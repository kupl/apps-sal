(n, a, b, c, d) = map(int, input().split())
ans = 0
for e in range(1, n + 1):
    min1 = a + b + e + 1
    max1 = a + b + e + n
    min2 = b + e + d + 1
    max2 = b + d + e + n
    min3 = d + c + e + 1
    max3 = d + c + e + n
    min4 = a + c + e + 1
    max4 = a + c + e + n
    l = max(min1, min2, min3, min4)
    r = min(max1, max2, max3, max4)
    if l <= r:
        ans += r - l + 1
print(ans)
