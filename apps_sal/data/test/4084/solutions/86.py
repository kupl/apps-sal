n, a, b = list(map(int, input().split()))

if n % (a + b) < a:
    ans = (n // (a + b)) * a + n % (a + b)
    print(ans)
else:
    ans = (n // (a + b)) * a + a
    print(ans)
