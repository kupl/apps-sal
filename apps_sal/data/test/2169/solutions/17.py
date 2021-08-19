def main():
    (h, w, d) = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    M = [[] for i in range(h * w)]
    for i in range(h):
        for j in range(w):
            M[a[i][j] - 1] = [i, j]
    dist = [0 for i in range(h * w)]
    for i in range(h * w):
        if i - d >= 0:
            dist[i] += dist[i - d] + abs(M[i][0] - M[i - d][0]) + abs(M[i][1] - M[i - d][1])
    q = int(input())
    for i in range(q):
        (l, r) = map(int, input().split())
        print(dist[r - 1] - dist[l - 1])


def __starting_point():
    main()


__starting_point()
