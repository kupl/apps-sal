from sys import stdin


def main():
    readline = stdin.readline
    (n, m) = map(int, readline().split())
    s = readline().strip()
    ans = []
    flag = False
    i = n
    while True:
        max_i = i
        for sa in range(1, m + 1):
            if i - sa == 0:
                ans.append(sa)
                flag = True
                break
            elif s[i - sa] == '0':
                max_i = i - sa
        if flag:
            break
        elif max_i != i:
            ans.append(i - max_i)
            i = max_i
        else:
            break
    if flag:
        ans.reverse()
        print(*ans)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
