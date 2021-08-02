n = int(input())
x = 1
y = n + 1
while y > x:
    mid = (x + y + 1) // 2
    if (mid + 1) * mid // 2 <= n + 1:
        x = mid
    else:
        y = mid - 1
print(n + 1 - y)
