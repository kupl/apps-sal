(n, a, b, c, d, e) = [int(input()) for _ in range(6)]
minVal = min(a, b, c, d, e)
if n // minVal == n / minVal:
    ans = n // minVal + 4
else:
    ans = n // minVal + 1 + 4
print(ans)
