a, b, c, n = map(int, input().split())
ans = 0
if a >= n:
    ans = n
elif a + b >= n:
    ans = a
elif a + b < n:
    ans = -(n - a - b) + a

print(ans)
