n, m = map(int, input().split())
A = list(map(int, input().split()))
k = sum(A)
if n >= k:
    print(n - k)
else:
    print(-1)
