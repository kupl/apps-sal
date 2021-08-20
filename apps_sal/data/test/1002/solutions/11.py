(n, d) = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
if s + 10 * (n - 1) > d:
    print(-1)
else:
    print((d - s) // 5)
