N, K = map(int, input().split())
A = {}
for i in range(N):
    a, b = map(int, input().split())
    A[a] = A.get(a, 0) + b
A = sorted(A.items())

cnt = 0
for n, k in A:
    cnt += k
    if cnt >= K:
        print(n)
        return
