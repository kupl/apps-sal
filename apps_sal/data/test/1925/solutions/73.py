a, b, n = map(int, input().split())

if n < b:
    ans = (a * n) // b - a * (n // b)
else:
    m = b - 1
    ans = (a * m) // b - a * (m // b)

print(ans)
