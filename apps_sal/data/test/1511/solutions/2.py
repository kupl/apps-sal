n, m, k = list(map(int, input().split()))
ans = [0 for i in range(n)]
lock = [False for i in range(k)]
deadlock = lock[:]
insset = [[0 for i in range(n)] for i in range(m)]
for i in range(n):
    ins = list(map(int, input().split()))
    for j in range(m):
        insset[j][i] = ins[j]
for r in range(m):
    ins = insset[r]
    for i, el in enumerate(ins):
        if el == 0 or ans[i]:
            continue
        if lock[el - 1]:
            deadlock[el - 1] = True
        else:
            lock[el - 1] = True
    for i in range(n):
        if ins[i] == 0 or ans[i]:
            continue
        if deadlock[ins[i] - 1]:
            ans[i] = r + 1
    lock = [False for i in range(k)]
for el in ans:
    print(el)
