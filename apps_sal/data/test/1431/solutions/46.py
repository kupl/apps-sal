N = int(input())
A = list(map(int, input().split()))
B = [0] * N

for i in range(N - 1, -1, -1):
    tmp_sum = 0
    for j in range((i + 1) * 2 - 1, N, i + 1):
        tmp_sum += B[j]
        tmp_sum %= 2
    B[i] = tmp_sum ^ A[i]

print(sum(B))
print(*[i + 1 for i, b in enumerate(B) if b == 1])
