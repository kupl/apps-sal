def main():
    mode = "filee"
    if mode == "file": f = open("test.txt", "r")
    get = lambda: [int(x) for x in (f.readline() if mode == "file" else input()).split()]
    gets = lambda: [str(x) for x in (f.readline()[:-1] if mode == "file" else input()).split(":")]
    [n, m, t] = get()
    [a, b] = [[0] * 20002, [0] * 20002]
    if n < m:
        print("No solution")
        return
    for i in range(1, n + 1):
        g = gets()
        a[i] = int(g[-1]) + int(g[1]) * 60 + int(g[0]) * 3600
    [p, count, sim, ist] = [1, 0, 0, False]
    for i in range(1, n + 1):
        while p < i and a[i] - t + 1 > a[p]:
            p += 1
            if b[p] != b[p - 1]:
                sim = max(sim - 1, 0)
        if a[i] < a[p] + t and sim < m:
            [count, sim] = [count + 1, sim + 1]
        if sim == m:
            ist = True
        b[i] = count
    if ist == False:
        print("No solution")
        return
    print(count)
    for i in range(1, n + 1):
        print(b[i], end=' ')

    if mode == "file": f.close()


def __starting_point():
    main()


__starting_point()
