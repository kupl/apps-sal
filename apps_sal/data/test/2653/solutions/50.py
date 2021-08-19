import sys
read = sys.stdin.read
sys.setrecursionlimit(10**7)
#readlines = sys.stdin.readlines


def main():
    def dfs(v, s):
        if notseen[v]:
            scores[v] += s
            notseen[v] = 0
            for nextv in gg[v]:
                dfs(nextv, scores[v])

    data = tuple(map(int, read().split()))
    n, q = data[0], data[1]
    gg = {i: set() for i in range(1, n + 1)}
    # 木なので”正しく”処理すればgg[x]へのaddは２回ではなく１回でいいはず。
    # だがうまく行かないため、無向グラフのように２回加えて、dfs関数で各頂点を１回しかみないように対応。
    for i1, v1 in zip(data[2:n * 2:2], data[3:n * 2:2]):
        gg[v1].add(i1)
        gg[i1].add(v1)
    scores = [0] * (n + 1)
    for j1, v1 in zip(data[n * 2::2], data[n * 2 + 1::2]):
        scores[j1] += v1

    notseen = [1] * (n + 1)
    dfs(1, 0)
    print(*scores[1:], sep=' ')


def __starting_point():
    main()


__starting_point()
