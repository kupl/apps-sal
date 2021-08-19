t = int(input())
ret = []
while t > 0:
    t -= 1
    (n, k, d1, d2) = map(int, input().split())
    y1 = (k - (d1 - d2)) // 3
    x1 = y1 + d1
    z1 = y1 - d2
    ans1 = 2 * x1 - (z1 + y1)
    if x1 + y1 + z1 == k and min(z1, y1) >= 0 and (ans1 <= n - k) and ((n - k - ans1) % 3 == 0):
        ret.append('yes')
        continue
    y1 = (k - (d1 + d2)) // 3
    x1 = y1 + d1
    z1 = y1 + d2
    if d1 >= d2:
        ans1 = 2 * x1 - (y1 + z1)
    else:
        ans1 = 2 * z1 - (y1 + x1)
    if x1 + y1 + z1 == k and y1 >= 0 and (ans1 <= n - k) and ((n - k - ans1) % 3 == 0):
        ret.append('yes')
        continue
    y1 = (k - (d2 - d1)) // 3
    x1 = y1 - d1
    z1 = y1 + d2
    ans1 = 2 * z1 - (x1 + y1)
    if x1 + y1 + z1 == k and min(x1, y1) >= 0 and (ans1 <= n - k) and ((n - k - ans1) % 3 == 0):
        ret.append('yes')
        continue
    y1 = (k + (d2 + d1)) // 3
    x1 = y1 - d1
    z1 = y1 - d2
    ans1 = 2 * y1 - (x1 + z1)
    if x1 + y1 + z1 == k and min(x1, z1) >= 0 and (ans1 <= n - k) and ((n - k - ans1) % 3 == 0):
        ret.append('yes')
        continue
    ret.append('no')
print(*ret, sep='\n')
