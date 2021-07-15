n, k = map(int, input().split())
t = list(map(int, input().split()))
s, p = [], [[] for i in range(max(t) + 1)]
for i, j in enumerate(t, 1): p[j].append(str(i))
if len(p[0]) - 1: print('-1')
else:
    for i in range(1, len(p)):
        if k * len(p[i - 1]) < len(p[i]):
            print('-1')
            return
        j, u, v = 0, len(p[i]) // k, len(p[i]) % k
        for x in range(u):
            s += [p[i - 1][x] + ' ' + p[i][y] for y in range(j, j + k)]
            j += k
        s += [p[i - 1][u] + ' ' + p[i][y] for y in range(j, j + v)]
        if i == 1: k -= 1
    print(len(s))
    print('\n'.join(s))
