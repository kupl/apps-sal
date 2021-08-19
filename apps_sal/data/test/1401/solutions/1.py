import sys


def main():
    u = []
    r = 0
    x = []
    q = []
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    links = [[] for i in range(n)]
    u = [False] * n
    p = [0] * n
    d = [False] * n
    data = sys.stdin.readlines()
    for i in range(n - 1):
        y = data[i].split()
        (v, c) = (int(y[0]) - 1, int(y[1]))
        links[i + 1].append((v, c))
        links[v].append((i + 1, c))
    u[0] = True
    q.append((0, 0, False))
    while len(q) != 0:
        z = q.pop()
        (i, path, al) = (z[0], z[1], z[2])
        for y in links[i]:
            (j, c) = (y[0], y[1])
            if not u[j]:
                u[j] = True
                al2 = al
                np = max(path + c, c)
                if np > x[j]:
                    al2 = True
                if al2:
                    r += 1
                q.append((j, np, al2))
    print(r)


main()
