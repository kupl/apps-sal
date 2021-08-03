import sys


def main():
    n, x = map(int, sys.stdin.readline().split())
    al = []
    starts = []
    finishes = []
    y = [-1] * 200002
    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        al.append((a, b, c))
        starts.append((a, i))
        finishes.append((b, i))

    finishes = sorted(finishes, key=lambda x: x[0])
    starts = sorted(starts, key=lambda x: x[0])
    j = 0

    res = 3 * (10**9)
    for i in range(n):
        while j < n and starts[j][0] <= finishes[i][0]:
            c = starts[j][1]
            h = al[c][1] - al[c][0] + 1
            cost = al[c][2]
            if y[x - h] != -1 and y[x - h] + cost < res:
                res = y[x - h] + cost
            j += 1
        c = finishes[i][1]
        h = al[c][1] - al[c][0] + 1
        cost = al[c][2]
        if y[h] == -1 or y[h] > cost:
            y[h] = cost

    if res == 3 * (10**9):
        print(-1)
    else:
        print(res)


main()
