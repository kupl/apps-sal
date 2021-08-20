def main():
    (n, x, m) = list(map(int, input().split()))
    tot = [x, x]
    for i in range(m):
        cur = list(map(int, input().split()))
        if tot[1] >= cur[0] >= tot[0] or tot[1] >= cur[1] >= tot[0] or (cur[1] >= tot[1] and cur[0] <= tot[0]):
            tot[0] = min(cur[0], tot[0])
            tot[1] = max(cur[1], tot[1])
    print(tot[1] - tot[0] + 1)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
