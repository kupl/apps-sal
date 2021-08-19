N = int(input())
A = list(map(int, input().split()))
B = [0] * (N + 1)
for i in range(N, 0, -1):
    B[i] = sum((B[x] for x in range(i, N + 1, i))) % 2 != A[i - 1]
print(sum(B))
print(*[i for (i, v) in enumerate(B) if v])
