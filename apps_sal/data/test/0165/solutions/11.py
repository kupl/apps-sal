(b, d, s) = map(int, input().split())
if b >= d and b >= s:
    ans = max(0, b - d - 1) + max(0, b - s - 1)
elif d >= s and d >= b:
    ans = max(0, d - s - 1) + max(0, d - b - 1)
else:
    ans = max(0, s - d - 1) + max(0, s - b - 1)
print(ans)
