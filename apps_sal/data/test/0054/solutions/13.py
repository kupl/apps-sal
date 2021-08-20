(n, m) = list(map(int, input().split()))
a = 0
d = True
for i in range(100):
    if d and n > 0:
        if m % n ** (a + 1) == n ** a:
            m -= n ** a
            a += 1
        elif m % n ** (a + 1) == 0:
            a += 1
        elif (m + n ** a) % n ** (a + 1) == 0:
            m += n ** a
            a += 1
        else:
            d = False
            print('NO')
if d:
    print('YES')
