import sys
(n, ma, mb) = map(int, input().split())
abc = []
for _ in range(n):
    (a, b, cost) = map(int, input().split())
    abc.append((a, b, cost))


def main():
    sa = 0
    sb = 0
    for i in range(n):
        sa += abc[i][0]
        sb += abc[i][1]
    res = [[float('infinity')] * (sb + 1) for _ in range(sa + 1)]
    res[0][0] = 0
    for (a, b, c) in abc:
        for j in range(sa, -1, -1):
            for k in range(sb, -1, -1):
                if j >= a and k >= b:
                    res[j][k] = min(res[j][k], res[j - a][k - b] + c)
    ans = float('infinity')
    for i in range(1, min(sa // ma, sb // mb) + 1):
        ans = min(ans, res[ma * i][mb * i])
    if ans == float('infinity'):
        return -1
    else:
        return ans


def __starting_point():
    ans = main()
    print(ans)


__starting_point()
