F = open('input.txt', 'r')


def I():
    return list(map(int, F.readline().split()))


(n, k) = I()
a = I()
m = sorted(range(1, n + 1), key=lambda x: a[x - 1])[-k:]
W = open('output.txt', 'w')
W.write(str(a[m[0] - 1]) + '\n' + ' '.join(map(str, m)))
W.close()
