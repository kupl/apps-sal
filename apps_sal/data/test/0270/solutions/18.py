"""
References
----------
[0]. 解説(公式), https://img.atcoder.jp/abc144/editorial.pdf, AtCoder
    - O(NM)
[1]. kmjp. AtCoder ABC 
    - O(NM)
[2]. physics0523. Fork in the Road(ABC144-F), <https://physics0523.hatenablog.com/entry/2019/10/27/235334>, physics0523's 精進ログ
    - O(M)
[3]. Genki Ogaki. BC144 F - Fork in the Road考察＋参戦記, <https://www.onakasuitacity.com/abc144-f>, おじさん、今日プロ始
めるってよ
    - O(M)
"""


def solve(n, m, s, t):
    edges = [[] for i in range(n)]
    for i in range(m):
        u, v = s[i], t[i]
        edges[u - 1].append(v - 1)
    p = [0] * n
    p[0] = 1
    for i in range(n):
        for j in edges[i]:
            p[j] += p[i] / len(edges[i])
    E = [0] * n
    for i in range(n - 2, -1, -1):
        v = [E[j] for j in edges[i]]
        E[i] = 1 + sum(v) / len(v)
    res = E[0]
    for i in range(n):
        deg = len(edges[i])
        if deg <= 1:
            continue
        k = max((E[j], j) for j in edges[i])[1]
        v = [E[j] for j in edges[i] if j != k]
        res = min(res, E[0] + p[i] * (sum(v) / (deg - 1) - E[k]) / deg)
    return res


n, m = map(int, input().split())
s = [0] * m
t = [0] * m
for i in range(m):
    s[i], t[i] = map(int, input().split())
print(solve(n, m, s, t))
