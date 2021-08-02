n = int(input())


def main(n):
    p = []
    q = []
    for i in range(2):
        p.append([0] * 1000)
    for i in range(2):
        q.append([0] * 1000)
    for i in range(n):
        x, y = list(map(int, input().split()))
        x1, y1, x2, y2 = x - 1, y - 1, x - 1, y - 1
        x1, y1 = x1 - min(x1, y1), y1 - min(x1, y1)
        if x1 == 0:
            p[1][y1] += 1
        else:
            p[0][x1] += 1
        while y2 < 999 and x2 > 0:
            x2 -= 1
            y2 += 1
        if y2 == 999:
            q[1][x2] += 1
        else:
            q[0][y2] += 1
    sum = 0
    for i in range(2):
        for t in range(1000):
            sum += (p[i][t] * (p[i][t] - 1)) // 2
    for i in range(2):
        for t in range(1000):
            sum += (q[i][t] * (q[i][t] - 1)) // 2
    print(sum)


main(n)
