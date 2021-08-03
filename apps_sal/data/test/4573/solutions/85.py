n = int(input())
xn = list(map(int, input().split()))
xn_s = sorted(xn)
m1 = xn_s[n // 2 - 1]
m2 = xn_s[n // 2]
for x in xn:
    if x <= m1:
        print(m2)
    else:
        print(m1)
