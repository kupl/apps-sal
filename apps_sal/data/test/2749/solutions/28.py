H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))


def main():
    ans = [[0] * W for _ in range(H)]
    color = 0
    num = 0
    for i in range(H):
        if i % 2 == 0:
            for j in range(W):
                ans[i][j] = color + 1
                num += 1
                if num == a[color]:
                    color += 1
                    num = 0
        else:
            for j in range(W - 1, -1, -1):
                ans[i][j] = color + 1
                num += 1
                if num == a[color]:
                    color += 1
                    num = 0
    for i in range(H):
        print(*ans[i])


def __starting_point():
    main()


__starting_point()
