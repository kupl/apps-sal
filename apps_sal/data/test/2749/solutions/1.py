def main():
    H, W = list(map(int, input().split(' ')))
    N = int(input())
    A = list(map(int, input().split(' ')))
    colors = list()
    for i, a in enumerate(A):
        c = i + 1
        for _ in range(a):
            colors.append(c)
    assert len(colors) == H * W
    ans = [[0 for _ in range(W)] for _ in range(H)]
    # 蛇腹状にぬっていく
    for i, c in enumerate(colors):
        w = i // H
        h = min([i % (2 * H), 2 * H - 1 - (i % (2 * H))])
        ans[h][w] = c
    for row in ans:
        print((' '.join(map(str, row))))


def __starting_point():
    main()

__starting_point()
