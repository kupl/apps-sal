(n, a, b) = map(int, input().split())
t = n // (a + b)
ans = t * a
s = n % (a + b)
if s <= a:
    ans += s
else:
    ans += a
print(ans)
