(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
x = m * n - sum(a)
if x <= k and x > 0:
    print(x)
elif x <= k:
    print(0)
else:
    print(-1)
