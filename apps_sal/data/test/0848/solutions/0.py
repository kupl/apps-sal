(n, k) = list(map(int, input().split()))
m = n + 1
if 2 * k > n - 1:
    print('-1')
else:
    t = []
    for i in range(1, k + 1):
        t += [str(j) + ' ' + str(j + i) for j in range(1, m - i)]
        t += [str(j) + ' ' + str(j + i - n) for j in range(m - i, m)]
    print(k * n)
    print('\n'.join(t))
