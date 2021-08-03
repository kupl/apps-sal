n = int(input())
A = list(map(int, input().split()))

B = [0 for i in range(n)]
B[n // 2:] = A[n // 2:]

for i in range(n // 2, 0, -1):
    B[i - 1] = (sum(B[i * 2 - 1::i]) % 2 != A[i - 1])

print(sum(B))
for i, j in enumerate(B):
    if j == 1:
        print(i + 1)
