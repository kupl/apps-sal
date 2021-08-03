def main():
    n = int(input())
    graph = [[] for i in range(n)]
    ans = [(0, 0)] * n

    for _ in range(n - 1):
        u, v = [int(el) for el in input().split()]
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    for l in graph:
        if len(l) > 4:
            print('NO')
            return

    step = 1 << 28

    used = [False] * n

    def dfs(v, direction, step, koord):
        used[v] = True
        if direction == 'u':
            my_koord = (koord[0] + step, koord[1])
            dirs = ['u', 'l', 'r']
        elif direction == 'd':
            my_koord = (koord[0] - step, koord[1])
            dirs = ['d', 'l', 'r']
        elif direction == 'l':
            my_koord = (koord[0], koord[1] - step)
            dirs = ['u', 'd', 'l']
        elif direction == 'r':
            my_koord = (koord[0], koord[1] + step)
            dirs = ['u', 'd', 'r']
        elif direction == '':
            my_koord = (0, 0)
            dirs = ['u', 'd', 'l', 'r']

        ans[v] = my_koord

        d = 0
        for u in graph[v]:
            if not used[u]:
                dfs(u, dirs[d], step >> 1, my_koord)
                d += 1

    dfs(0, '', step, (0, 0))

    print('YES')
    for k in ans:
        print(k[0], k[1])


main()
