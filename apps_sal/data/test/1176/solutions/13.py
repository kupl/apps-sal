N = int(input())
A = list(map(int, input().split()))

souwa = 0
cnt = 0
keep = 1e10

for i in range(N):
    if A[i] < 0:
        cnt += 1
        A[i] *= (-1)

    souwa += A[i]
    keep = min(keep, A[i])

print((souwa - 2 * keep * (cnt % 2)))
