a, b, c, k = list(map(int, input().split()))
ans = 0
if a >= k:
    ans = k * 1
else:
    ans = a * 1 + max(0, (k - a)) * 0 + max(0, (k - a - b)) * (-1)
print(ans)
