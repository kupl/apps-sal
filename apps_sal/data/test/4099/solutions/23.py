(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
b = m * n - sum(a)
if 0 <= b <= k:
    print(b)
elif b < 0:
    print(0)
else:
    print(-1)
