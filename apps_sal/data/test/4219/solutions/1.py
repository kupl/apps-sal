N = int(input())
A = [[] for _ in range(N)]
for i in range(N):
    for _ in range(int(input())):
        A[i].append(list(map(int, input().split())))
ans = []
for i in range(2 ** N):
    Bit = [1] * N
    for j in range(N):
        if i >> j & 1:
            Bit[j] = 0
    i = 0
    no = 0
    while i < N:
        if Bit[i] == 1:
            for (x, y) in A[i]:
                if Bit[x - 1] != y:
                    no = 1
        i += 1
    if no:
        ans.append(0)
    else:
        ans.append(Bit.count(1))
print(max(ans))
