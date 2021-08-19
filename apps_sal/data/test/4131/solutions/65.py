(n, m) = list(map(int, input().split()))
ken = [1 for i in range(n + 1)]
inf = [[] for i in range(m)]


def f(x):
    m = 0
    while x > 0:
        m += 1
        x = x // 10
    return m


for i in range(m):
    (p, y) = list(map(int, input().split()))
    inf[i].append(i + 1)
    inf[i].append(p)
    inf[i].append(y)
inf = sorted(inf, key=lambda x: x[2])
for i in range(m):
    inf[i].append(ken[inf[i][1]])
    ken[inf[i][1]] += 1
inf = sorted(inf)
for i in range(m):
    ans = ''
    p = inf[i][1]
    y = inf[i][3]
    for j in range(6 - f(p)):
        ans += '0'
    ans = ans + str(p)
    for j in range(6 - f(y)):
        ans = ans + '0'
    ans = ans + str(y)
    print(ans)
