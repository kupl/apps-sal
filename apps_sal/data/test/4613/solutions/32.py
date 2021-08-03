import itertools
# 入力
N, M = list(map(int, input().split()))
ABs = [list(map(int, input().split())) for _ in range(M)]

# 橋はMAX50本なので、1本ずつ取り除いて全てが繋がるかどうかを試行する。

# UnionFind木


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])  # 経路圧縮
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y
    size[y] = size[x] + size[y]
    size[x] = 0


# 橋の組み合わせ
loop_list = list(itertools.combinations(ABs, M - 1))
# print(loop_list)

ans = 0
for loop in loop_list:
    # ループ毎にリセットするので。良くない気がする。
    par = [i for i in range(N + 1)]
    size = [1 for _ in range(N + 1)]

    for bridge in loop:
        unite(bridge[0], bridge[1])

#    print(par)
#    print(size)
    if(max(size) != N):
        ans += 1

print(ans)
