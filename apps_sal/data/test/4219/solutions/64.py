N = int(input())
testimo_ls = [[] for i in range(N)]
rst = 0
for i in range(N):
    A = int(input())
    for j in range(A):
        (x, y) = map(int, input().split(' '))
        testimo_ls[i].append([x - 1, y])
for i in range(1 << N):
    honest_ls = []
    for j in range(N):
        if i >> j & 1:
            honest_ls.append(j)
    is_ok = True
    for s in honest_ls:
        for t in testimo_ls[s]:
            if t[0] not in honest_ls and t[1] == 1:
                is_ok = False
                break
            if t[0] in honest_ls and t[1] == 0:
                is_ok = False
                break
    if is_ok:
        rst = max(rst, len(honest_ls))
print(rst)
