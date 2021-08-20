import sys
import operator


def solve():
    a = [int(x) for x in input().split()]
    n = int(input())
    b = [int(x) for x in input().split()]
    have = []
    arr_append = have.append
    for i in range(0, n):
        for j in range(0, 6):
            arr_append([b[i] - a[j], i])
    cnt = [0] * n
    z = n
    sz = len(have)
    ans = 999999999999
    r = 0
    have.sort(key=operator.itemgetter(0))
    for i in range(0, sz):
        while r < sz and z > 0:
            cnt[have[r][1]] += 1
            if cnt[have[r][1]] == 1:
                z -= 1
            r += 1
        if z > 0:
            break
        ans = min(ans, have[r - 1][0] - have[i][0])
        cnt[have[i][1]] -= 1
        if cnt[have[i][1]] == 0:
            z += 1
    print(ans)


def main(argv):
    solve()


def __starting_point():
    main(sys.argv)


__starting_point()
