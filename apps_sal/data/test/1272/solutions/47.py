import sys
n, m = list(map(int, input().split()))
ab = [[0, 0] for i in range(m)]
for i in range(m):
    ab[i][0], ab[i][1] = list(map(int, input().split()))

sys.setrecursionlimit(10**9)  # 再帰の上限をあげる

root = [-1 for i in range(n + 1)]  # 自分が親なら自身の番号を、そうでないなら（元）親の番号を示す


def r(x):  # 親は誰？
    if root[x] < 0:
        return x
    else:
        root[x] = r(root[x])
        return root[x]


ans = n * (n - 1) // 2
d = [n * (n - 1) // 2]
for i in range(1, m + 1):
    a, b = ab[-i][0], ab[-i][1]
    a = r(a)
    b = r(b)
    a, b = min(a, b), max(a, b)
    if a != b:
        ans -= root[a] * root[b]
        root[a] += root[b]
        root[b] = a
    d.append(ans)

for i in range(m):
    print((d[-2 - i]))
