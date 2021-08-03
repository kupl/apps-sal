
def main():
    n, m, x = map(int, input().split(" "))
    ca = []
    a = []
    c = []
    INF = 1e7
    ans = INF
    for i in range(n):
        ca.append(list(map(int, input().split(" "))))
    for i in range(n):
        c.append(ca[i][0])
        a.append(ca[i][1:])
    for i in range(1 << n):
        a_sum = [0] * m
        c_sum = 0
        for j in range(n):
            if i >> j & 1 == 1:
                for k in range(m):
                    a_sum[k] += a[j][k]
                c_sum += c[j]
        if min(a_sum) >= x and c_sum < ans:
            ans = c_sum
    if ans == INF:
        print(-1)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
