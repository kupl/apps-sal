n, a, b = list(map(int, input().split()))
ans = (n // (a + b)) * a
rem = n % (a + b)
if rem < a:
    ans += rem
else:
    ans += a
print(ans)
