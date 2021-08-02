visited = [False] * 105
p = {}


def dfs(i):
    nonlocal visited
    nonlocal p
    if visited[i] == True:
        return
    visited[i] = True
    for j in p[i]:
        dfs(j)


def main():
    nonlocal visited
    nonlocal p
    mode = "filee"
    if mode == "file": f = open("test.txt", "r")
    get = lambda: [int(x) for x in (f.readline() if mode == "file" else input()).split()]
    [n] = get()
    g = [[0]]
    le = 0
    for z in range(n):
        [t, x, y] = get()
        if t == 1:
            g.append([x, y])
            le += 1
            p[le] = []
            for i in range(1, le):
                [a, b] = [g[i][0], g[i][1]]
                if (x < a and a < y) or (x < b and b < y):
                    p[i].append(le)
                if (a < x and x < b) or (a < y and y < b):
                    p[le].append(i)
        else:
            for i in range(105):
                visited[i] = False
            dfs(x)
            print("YES" if visited[y] == True else "NO")

    if mode == "file": f.close()


def __starting_point():
    main()


__starting_point()
