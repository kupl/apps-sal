a, b, c, d = list(map(int, input().split()))
dd = d / b
if dd > c:
    print(c * a)
else:
    cnt = a // b
    cnt2 = a % b
    print(min(cnt * d + cnt2 * c, (cnt + 1) * d))
