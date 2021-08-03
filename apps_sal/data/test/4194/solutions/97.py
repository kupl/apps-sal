n, m = map(int, input().split())
L = list(map(int, input().split()))

A = sum(L)

if n >= A:
    print(n - A)
else:
    print(-1)
