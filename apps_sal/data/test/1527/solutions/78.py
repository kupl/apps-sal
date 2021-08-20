import queue


def main():
    (h, w) = list(map(int, input().split()))
    st = [[1] * (w + 2) for _ in range(h + 2)]
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '.':
                st[i + 1][j + 1] = 0
    ans = 0
    for i in range(1, h + 2):
        for j in range(1, w + 2):
            if st[i][j] == 0:
                fs = [[float('inf')] * (w + 2) for _ in range(h + 2)]
                q = queue.Queue()
                fs[i][j] = 0
                q.put([i, j])
                while not q.empty():
                    (y, x) = q.get()
                    if st[y - 1][x] == 0 and fs[y - 1][x] > fs[y][x] + 1:
                        fs[y - 1][x] = fs[y][x] + 1
                        q.put([y - 1, x])
                    if st[y + 1][x] == 0 and fs[y + 1][x] > fs[y][x] + 1:
                        fs[y + 1][x] = fs[y][x] + 1
                        q.put([y + 1, x])
                    if st[y][x - 1] == 0 and fs[y][x - 1] > fs[y][x] + 1:
                        fs[y][x - 1] = fs[y][x] + 1
                        q.put([y, x - 1])
                    if st[y][x + 1] == 0 and fs[y][x + 1] > fs[y][x] + 1:
                        fs[y][x + 1] = fs[y][x] + 1
                        q.put([y, x + 1])
                    if ans < fs[y][x]:
                        ans = fs[y][x]
    print(ans)


def __starting_point():
    main()


__starting_point()
