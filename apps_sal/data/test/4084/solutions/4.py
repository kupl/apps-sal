n, a, b = map(int, input().split())

ans = n // (a + b) * a
rem = n % (a + b)
ans += min(rem, a)

print(ans)
