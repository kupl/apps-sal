N = int(input())
A = list(map(int, input().split()))
B = [0] * N

for i in range(N - 1, -1, -1):
    B[i] = (sum(B[2 * (i + 1) - 1::i + 1]) % 2) ^ A[i]

print(sum(B))
print(*[i+1 for i in range(N) if B[i] == 1])
