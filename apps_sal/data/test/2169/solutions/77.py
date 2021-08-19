def main():
    (h, w, d) = list(map(int, input().split()))
    ans = [[0] for _ in range(d)]
    s = [0] * d
    ans[0].append(0)
    dict = {}
    for i in range(h):
        for (j, a) in enumerate(list(map(int, input().split()))):
            dict[a] = (i, j)
    for i in range(1, h * w + 1 - d):
        m = i % d
        s[m] += abs(dict[i][0] - dict[i + d][0]) + abs(dict[i][1] - dict[i + d][1])
        ans[m].append(s[m])
    q = int(input())
    for _ in range(q):
        (l, r) = list(map(int, input().split()))
        m = l % d
        print(ans[m][r // d] - ans[m][l // d])


def __starting_point():
    main()


__starting_point()
