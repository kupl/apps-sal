N, M = map(int, input().split())
l = [0] * M
for i in range(N):
    A = list(map(int, input().split()))
    K = A[0]
    A = A[1:]
    for j in range(K):
        l[A[j] - 1] += 1
print(l.count(N))
