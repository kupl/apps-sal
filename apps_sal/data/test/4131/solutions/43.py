import bisect
(n, m) = map(int, input().split(' '))
py = [list(map(int, input().split(' '))) for i in range(m)]
n_py = sorted(py)
a = [[] for i in range(n + 1)]
for (i, j) in py:
    a[i].append(j)
for i in range(1, n + 1):
    a[i] = sorted(a[i])
for (i, j) in py:
    (ix, ij) = map(str, [i, bisect.bisect(a[i], j)])
    print('0' * (6 - len(ix)) + ix + '0' * (6 - len(ij)) + ij)
