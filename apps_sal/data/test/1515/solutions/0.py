(p, k) = map(int, input().split())
u = 10 * k - 1
v = pow(10, p - 1, u) - k
for y in range(k, 10):
    if y * v % u == 0:
        q = d = 9 * y
        while q % u:
            q = 10 * q + d
        q = str(q // u)
        print(q * (p // len(q)))
        break
else:
    print('Impossible')
