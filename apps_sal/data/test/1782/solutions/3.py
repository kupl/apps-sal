(n, k) = map(int, input().split())
if n < 3 * k:
    print(-1)
else:
    t = list((str(i) + ' ' for i in range(1, k + 1)))
    print(''.join(t) + ''.join((i * 2 for i in t)) + t[-1] * (n - 3 * k))
