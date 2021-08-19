(n, a, b) = map(int, input().split())
c = n // (a + b)
if n % (a + b) >= a:
    ans = a * (c + 1)
else:
    ans = a * c + n % (a + b)
print(ans)
