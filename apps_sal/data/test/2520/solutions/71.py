import sys
n, m, k = list(map(int, input().split()))

sys.setrecursionlimit(10**9)  # 再帰の上限をあげる

root = [-1 for i in range(n + 1)]  # 自分が親ならグループの人数のマイナス倍を、そうでないなら（元）親の番号を示す


def r(x):  # 親は誰？
    if root[x] < 0:
        return x
    else:
        root[x] = r(root[x])
        return root[x]


def unite(x, y):
    x = r(x)
    y = r(y)
    if x == y:
        return
    if x > y:
        x, y = y, x
    root[x] += root[y]
    root[y] = x


fre = [[] for _ in range(n + 1)]
bro = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = list(map(int, input().split()))
    unite(a, b)
    fre[a].append(b)
    fre[b].append(a)

for i in range(k):
    a, b = list(map(int, input().split()))
    bro[a].append(b)
    bro[b].append(a)

ans = []
for i in range(1, n + 1):
    anser = -root[r(i)] - 1
    anser -= len(fre[i])
    for j in bro[i]:
        if r(i) == r(j):
            anser -= 1
    ans.append(str(anser))
print((" ".join(ans)))
