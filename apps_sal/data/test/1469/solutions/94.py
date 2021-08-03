import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    L = int(input())
    edges = []
    vertex = 1
    flag = True
    before = -1
    for i in range(19, -1, -1):
        if (L >> i) & 1:
            if flag:
                flag = False
                vertex = i + 1
                for j in range(1, vertex):
                    edges.append((j, j + 1, 0))
                    edges.append((j, j + 1, 1 << (j - 1)))
                before = 1 << i
            else:
                edges.append((i + 1, vertex, before))
                before += 1 << i
    print(vertex, len(edges))
    for t in edges:
        print(*t)


def __starting_point():
    main()


__starting_point()
