def main():
    n = int(input())
    ki = {}
    for i in range(1, n + 1):
        ki[i] = []
    for i in range(n - 1):
        (u, v, w) = list(map(int, input().split()))
        ki[u] += [[v, w % 2]]
        ki[v] += [[u, w % 2]]
    cl = [-1 for i in range(n)]
    cl[0] = 0
    que = [0]
    while len(que) > 0:
        q = que.pop(0)
        for v in ki[q + 1]:
            if cl[v[0] - 1] != -1:
                continue
            if v[1] == 1:
                cl[v[0] - 1] = (cl[q] + 1) % 2
                que.append(v[0] - 1)
            else:
                cl[v[0] - 1] = cl[q]
                que.append(v[0] - 1)
    for i in range(n):
        print(cl[i])


def __starting_point():
    main()


__starting_point()
