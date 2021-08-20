(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) + k < m * n:
    print(-1)
elif sum(a) >= m * n:
    print(0)
else:
    print(m * n - sum(a))
