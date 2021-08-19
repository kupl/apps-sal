(A, B, C) = map(int, input().split())
K = int(input())
X = sorted([A, B, C])
for _ in range(K):
    X[-1] *= 2
print(sum(X))
