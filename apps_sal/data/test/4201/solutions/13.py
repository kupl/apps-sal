def main():
    H, W, K = map(int, input().split())
    grid = [input() for _ in range(H)]

    n = H + W
    ans = 0
    for case in range(2**n):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if (case >> i) & 1:
                    if (case >> j + H) & 1:
                        if grid[i][j] == "
                        cnt += 1
        if cnt == K:
            ans += 1
    print(ans)


main()
