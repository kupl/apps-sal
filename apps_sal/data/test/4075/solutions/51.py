from itertools import combinations


def getval():
    n, m = map(int, input().split())
    s = [list(map(int, input().split())) for i in range(m)]
    for i in range(m):
        for j in range(1, s[i][0] + 1):
            s[i][j] -= 1
    p = list(map(int, input().split()))
    return n, m, s, p


def main(n, m, s, p):
    l = [[] for i in range(n)]
    for i in range(m):
        for j in range(1, s[i][0] + 1):
            l[s[i][j]].append(i)
    ans = 0
    for i in range(n + 1):
        for c in combinations(range(n), i):
            temp = [0 for i in range(m)]
            for j in c:
                for k in l[j]:
                    temp[k] += 1
                    temp[k] %= 2
            if temp == p:
                ans += 1
    print(ans)


def __starting_point():
    n, m, s, p = getval()
    main(n, m, s, p)


__starting_point()
