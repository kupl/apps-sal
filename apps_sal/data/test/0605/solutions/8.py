def f(p, t):
    return max(3 * p // 10, p - p * t // 250)


(a, b, c, d) = list(map(int, input().split()))
(m, v) = (f(a, c), f(b, d))
if v == m:
    print('Tie')
elif v > m:
    print('Vasya')
else:
    print('Misha')
