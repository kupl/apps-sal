def HOD(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    return a


(n, m, k) = map(int, input().split())
x = HOD(n, k)
n1 = n // x
k = k // x
x = HOD(m, k)
m1 = m // x
k = k // x
if k > 2:
    print('NO')
if k == 2:
    print('YES')
    print(0, 0)
    print(n1, 0)
    print(0, m1)
if k == 1:
    if n1 * 2 <= n:
        print('YES')
        print(0, 0)
        print(n1 * 2, 0)
        print(0, m1)
    elif m1 * 2 <= m:
        print('YES')
        print(0, 0)
        print(n1, 0)
        print(0, m1 * 2)
    else:
        print('NO')
