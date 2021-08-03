n, k = map(int, input().strip().split())

if 2 * k > (n - 1):

    print('-1')

else:

    r = [str(n * k)]

    for i in range(1, n + 1):

        for j in range(k):
            r.append(str(i) + ' ' + str((i + j) % n + 1))

    print('\n'.join(r))
