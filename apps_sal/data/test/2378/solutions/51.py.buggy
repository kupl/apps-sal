import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
MOD = 10**9 + 7
tree = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 頂点1をルートにして各頂点より下にある部分木の頂点数を求めていく
root, par = 1, 0
sizes = [0] * (N + 1)
order = [[root, par]]


def calc_nums(node, par):
    nonlocal sizes
    nonlocal order
    if sizes[node] > 0:
        return sizes[node]
    children = tree[node]
    res = 1
    for child in children:
        if child == par:
            continue
        order.append([child, node])
        res += calc_nums(child, node)
    sizes[node] = res
    return res


_ = calc_nums(root, par)

# 2の累乗を事前に計算しておく
prod2 = [1]
for i in range(N):
    prod2.append(prod2[-1] * 2 % MOD)

# 各頂点について、その頂点が穴あき度としてカウントされる状況を独立に計算する
demo = 0  # 分子
div = prod2[N]  # 分母
base = prod2[N - 1] - 1
for node, par in order:
    children = tree[node]
    num = base
    num_par = N - 1
    for child in children:
        if child == par:
            continue
        s = sizes[child]
        num_par -= s
        num -= prod2[s] - 1
    num -= prod2[num_par] - 1
    demo += num

ans = demo * pow(div, MOD - 2, MOD) % MOD
print(ans)
