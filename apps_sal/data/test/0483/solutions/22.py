3
inf = 1000000000.0


def main():
    n = int(input())
    dir = input()
    coords = list(map(int, input().split()))
    res = inf
    maxr = -1
    for i in range(n):
        if dir[i] == 'R':
            maxr = coords[i]
        elif maxr != -1:
            res = min((coords[i] - maxr) / 2, res)
    if res == inf:
        print(-1)
    else:
        print(int(res))


main()
