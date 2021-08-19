n = int(input())
x = 1
y = n * 2
while y - x > 1:
    mid = (y + x) // 2
    s = (1 + mid) * mid // 2
    if s > n + 1:
        y = mid
    else:
        x = mid
k = x
ans = 1 + (n - k)
print(ans)
