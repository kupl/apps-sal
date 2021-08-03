def main():
    N, M, X = list(map(int, input().split()))
    ca = [list(map(int, input().split())) for _ in range(N)]

    mincost = 12 * 10**5
    flag = 0
    for i in range(1, 2**N):
        lev = [0] * M
        cost = 0
        a = list((("0" * N) + bin(i)[2:])[-N:])
        for j in range(N):
            if a[j] == "1":
                cost += ca[j][0]
                for k in range(M):
                    lev[k] += ca[j][k + 1]
        if min(lev) >= X:
            mincost = min(mincost, cost)
            flag = 1
    if flag == 0:
        print((-1))
    else:
        print(mincost)


main()
