(s, p) = map(int, input().split())
Del = s * s - 4 * p
m = (s + Del ** (1 / 2)) / 2
m2 = (s - Del ** (1 / 2)) / 2
if int(m) == m and int(m2) == m2 and (m > 0) and (m2 > 0):
    print('Yes')
else:
    print('No')
