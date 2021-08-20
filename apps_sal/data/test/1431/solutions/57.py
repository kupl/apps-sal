N = int(input())
A = list(map(int, input().split()))
A = [0] + A
res = [0] * (N + 1)
M = 0
for i in range(N, 0, -1):
    if sum((res[j] for j in range(i, N + 1, i))) % 2 != A[i]:
        res[i] = 1
        M += 1
print(M)
print(*[k for (k, r) in enumerate(res) if r])
