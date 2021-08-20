def main():
    (n, m) = list(map(int, input().split()))
    w = list(map(int, input().split()))
    lv = [list(map(int, input().split())) for _ in [0] * m]
    min_v = 10 ** 15
    for (l, v) in lv:
        min_v = min(min_v, v)
    if min_v < max(w):
        print(-1)
        return 0
    w_list = [-1]
    l_list = [0]
    lv.sort(key=lambda x: (x[1], -x[0]))
    for (l, v) in lv:
        if w_list[-1] != v:
            w_list.append(v)
            l_list.append(max(l, l_list[-1]))
        else:
            l_list[-1] = max(l, l_list[-1])
    from itertools import permutations
    from bisect import bisect_left as bl
    perm = permutations(w)
    ans = 10 ** 15
    for p in perm:
        d = [[0] * n for _ in [0] * n]
        for i in range(n - 1):
            for j in range(i + 1, n):
                weight = sum(p[i:j + 1])
                b = bl(w_list, weight) - 1
                d[i][j] = max(d[i][j], l_list[b])
        dist = [0] * n
        for i in range(1, n):
            for j in range(i):
                if dist[i] - dist[j] < d[j][i]:
                    dist[i] = dist[j] + d[j][i]
        ans = min(ans, dist[-1])
    print(ans)


main()
