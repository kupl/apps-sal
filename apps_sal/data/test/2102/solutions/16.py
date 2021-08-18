import sys
import operator
import array


def solve():
    a = (list(map(int, input().split())))

    n = int(input())

    b = (list(map(int, input().split())))

    lad = [[]] * (n * 6)
    c = 0
    for i in range(0, n):
        for j in range(0, 6):
            lad[c] = (b[i] - a[j], i)
            c += 1

    lad.sort(key=operator.itemgetter(0))

    cnt = array.array('L', [0]) * n

    z = n
    ladcnt = len(lad)
    ans = 999999999999
    r = 0

    for i in range(0, ladcnt):
        while (r < ladcnt) and (z > 0):
            cnt[lad[r][1]] += 1
            if (cnt[lad[r][1]] == 1):
                z -= 1

            r += 1

        if (z > 0):
            break

        ans = min(ans, lad[r - 1][0] - lad[i][0])
        cnt[lad[i][1]] -= 1
        if (cnt[lad[i][1]] == 0):
            z += 1

    print(ans)


def main(argv):
    solve()


def __starting_point():
    main(sys.argv)


__starting_point()
