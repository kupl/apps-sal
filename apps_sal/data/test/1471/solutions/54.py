from collections import deque
n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    (u, v, w) = list(map(int, input().split()))
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))
'\nex.\n3\n1 2 2\n2 3 1\nの場合、g = [[(1, 2)], [(0, 2), (2, 1)], [(1, 1)]]\n'
'\n根から各頂点への距離をd_iとする\nu,vという2頂点について、その最小共通祖先をwとすると\nuとvの距離=d_u+d_v-2d_w\n第3項は常に偶数\nd_uとd_vの偶奇が等しければ全体は偶数、偶奇が異なれば全体は奇数\n例えば、d_iが偶数なら白に、奇数なら黒に塗るとすれば条件を満たす\n'
dq = deque([0])
ds = [-1] * n
ds[0] = 0
while dq:
    t = dq.popleft()
    for i in g[t]:
        if ds[i[0]] == -1:
            ds[i[0]] = ds[t] + i[1]
            dq.append(i[0])
for i in ds:
    if i % 2 == 0:
        print(0)
    else:
        print(1)
