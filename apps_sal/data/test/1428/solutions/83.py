def main():
    from sys import stdin

    def input():
        return stdin.readline().strip()

    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]

    '''
    for k in range(c):
        for i in range(c):
            for j in range(c):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    '''

    color = [list(map(int, input().split())) for _ in range(n)]

    counters = [[0] * c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            counters[(i + j) % 3][color[i][j] - 1] += 1

    cost = []
    for group in counters:
        l = []
        for i in range(c):
            num = 0
            for j in range(c):
                num += d[j][i] * group[j]
            l.append((num, i))
        l.sort()
        cost.append(l[:3])

    ans = 10 ** 9
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if cost[0][i][1] != cost[1][j][1] and cost[1][j][1] != cost[2][k][1] and cost[2][k][1] != cost[0][i][1]:
                    if ans > cost[0][i][0] + cost[1][j][0] + cost[2][k][0]:
                        ans = cost[0][i][0] + cost[1][j][0] + cost[2][k][0]

    print(ans)


main()
