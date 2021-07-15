N, K = list(map(int, input().split()))

dst = [1] * N

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))

    for j in range(d):
        dst[A[j]-1] = 0

print((sum(dst)))

