A = list(map(int, input().split()))
K = int(input())
for _ in range(K):
    A[A.index(max(A))] *= 2

print(sum(A))
