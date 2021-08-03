def main():
    n = int(input())
    p = list(map(int, input().split()))
    x = list(map(int, input().split()))

    child = [[] for _ in [0] * n]
    for i, j in enumerate(p):
        child[j - 1].append(i + 1)

    other = [0] * n

    for i in range(n - 1, -1, -1):
        if child[i] == []:
            continue
        dp = [-1] * (x[i] + 1)
        dp[0] = 0
        xx = x[i]
        for j in child[i]:
            dp2 = [-1] * (xx + 1)
            m = x[j]
            o = other[j]
            for k, l in enumerate(dp):
                if l == -1:
                    continue
                if k + m <= xx:
                    if dp2[k + m] != -1:
                        dp2[k + m] = min(dp2[k + m], l + o)
                    else:
                        dp2[k + m] = l + o
                if k + o <= xx:
                    if dp2[k + o] != -1:
                        dp2[k + o] = min(dp2[k + o], l + m)
                    else:
                        dp2[k + o] = l + m
            dp = dp2
        k = [j for j in dp if j != -1]
        if k != []:
            other[i] = min(k)
        else:
            print("IMPOSSIBLE")
            break
    else:
        print("POSSIBLE")


def __starting_point():
    main()


__starting_point()
