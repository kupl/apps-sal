n, a, b = list(map(int, input().split()))
line = n // (a + b)
remain = n % (a + b)

ans = line * a
ans += min(a, remain)

print(ans)

