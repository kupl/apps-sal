a, b, x = map(int, input().split())

ar = a % x
n = b - a + 1
if ar != 0:
    n -= x - ar

ans = n // x
if n % x >= 1:
    ans += 1

print(ans)
