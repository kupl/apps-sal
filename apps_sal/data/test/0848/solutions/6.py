import sys

f = sys.stdin

n, k = list(map(int, f.readline().strip().split()))


if 2 * k > (n - 1):

    print('-1')

else:

    r = [str(n * k)]

    for i in range(n):

        for j in range(k):

            r.append(str(i + 1) + ' ' + str((i + j + 1) % n + 1))

    print('\n'.join(r))
