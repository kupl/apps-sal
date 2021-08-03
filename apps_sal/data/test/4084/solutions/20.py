n, a, b = map(int, input().split())
ans = int(n / (a + b)) * a
if n % (a + b) <= a:
    print(ans + n % (a + b))
else:
    print(ans + a)
