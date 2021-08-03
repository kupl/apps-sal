n, k, m = map(int, input().split())
a = list(map(int, input().split()))
x = m * n - sum(a)
if x > k:
    print(-1)
elif x > 0:
    print(x)
else:
    print(0)
