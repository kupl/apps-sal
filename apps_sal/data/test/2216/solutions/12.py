(n, m, k) = [int(x) for x in input().split()]


def walk(n, m):
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                yield (i + 1, j + 1)
        else:
            for j in range(m - 1, -1, -1):
                yield (i + 1, j + 1)


w = walk(n, m)
for s in range(k - 1):
    print('2 ', end='')
    print('{} {} '.format(*next(w)), end='')
    print('{} {}'.format(*next(w)), end='')
    print()
r = []
while True:
    try:
        r.append(next(w))
    except StopIteration as e:
        break
print('{} '.format(len(r)), end='')
for i in r:
    print('{} {} '.format(*i), end='')
print()
