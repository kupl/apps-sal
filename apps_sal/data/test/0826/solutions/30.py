n = int(input())

x = 1
y = n*2
while y - x > 1:
    mid = (y + x) // 2
    s = (1 + mid) * mid // 2
    # print(x, y, mid, s)
    if s > n + 1:
        y = mid
    else:
        x = mid
k = x
# k = int((-1 + (1 + 8 * (n + 1)) ** 0.5) / 2)
# print(k)
ans = 1 + (n - k)
print(ans)

