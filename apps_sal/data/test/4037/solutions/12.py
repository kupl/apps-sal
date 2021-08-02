from functools import reduce


def doProject(r, proj, nproj):
    count = 0
    for i in range(len(proj)):
        if(proj[i][0] <= r):
            r += proj[i][1]
            count += 1
        else:
            pass

    dp = [[0 for j in range(r + 1)] for i in range(len(nproj) + 1)]
    dp[0][r] = count

    for i in range(len(nproj)):
        for cr in range(r + 1):
            if(nproj[i][0] <= cr and cr + nproj[i][1] >= 0):
                dp[i + 1][cr + nproj[i][1]] = max(dp[i + 1][cr + nproj[i][1]], dp[i][cr] + 1)

            dp[i + 1][cr] = max(dp[i + 1][cr], dp[i][cr])

    count = reduce(lambda x, y: max(x, y), dp[len(nproj)])

    return count


def main():

    n, r = map(int, input().rstrip().split())

    proj, nproj = [], []
    for _ in range(n):

        temp = list(map(int, input().rstrip().split()))

        if(temp[1] < 0):
            nproj.append(temp)
        else:
            proj.append(temp)

    proj.sort()
    nproj.sort(reverse=True, key=lambda x: x[0] + x[1])

    ans = doProject(r, proj, nproj)
    print(ans)


def __starting_point():
    main()


__starting_point()
