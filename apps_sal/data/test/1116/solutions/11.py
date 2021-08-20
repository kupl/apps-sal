import math
T = int(input())
for i in range(T):
    (r, b, k) = map(int, input().split())
    if r == b:
        print('OBEY')
        continue
    if r > b:
        tem = r
        r = b
        b = tem
    gicd = math.gcd(r, b)
    out = int((b + r - gicd - 1) / r)
    if out >= k:
        print('REBEL')
    else:
        print('OBEY')
