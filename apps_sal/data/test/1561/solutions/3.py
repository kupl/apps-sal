def main():
    n, m, k = map(int, input().split())
    g = []
    for i in range(n):
        g.append(input())
    ans = 0
    if k == 1:
        cnt = 0
        for i in range(n):
            for j in range(m):
                cnt += 1 if g[i][j] == '.' else 0
        print(cnt)
        return
    # count row
    for i in range(n):
        cnt = 0
        for j in range(m):
            if g[i][j] == '.':
                cnt += 1
                if cnt >= k:
                    ans += 1
            else:
                cnt = 0
    for j in range(m):
        cnt = 0
        for i in range(n):
            if g[i][j] == '.':
                cnt += 1
                if cnt >= k:
                    ans += 1
            else:
                cnt = 0
    print(ans)


def __starting_point():
    main()
__starting_point()
