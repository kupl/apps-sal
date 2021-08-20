from fractions import gcd
ans = False
x1 = 0
y1 = 0
y2 = 0
x3 = 0
(n, m, k) = input().split(' ')
n = int(n)
m = int(m)
k = int(k)
a = gcd(n, k)
n_new = n / a
k_new = k / a
a = gcd(m, k_new)
m_new = m / a
k_new = k_new / a
if k_new > 2:
    print('NO')
else:
    x2 = int(n_new)
    y3 = int(m_new)
    if k_new < 2:
        if x2 * 2 <= n:
            x2 *= 2
            ans = True
        elif y3 * 2 <= m:
            y3 *= 2
            ans = True
        else:
            print('NO')
    else:
        ans = True
    if ans:
        print('YES')
        print(x1, y1)
        print(x2, y2)
        print(x3, y3)
