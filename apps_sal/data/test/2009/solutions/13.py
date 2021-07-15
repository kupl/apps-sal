from sys import setrecursionlimit
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(67108864)


def main():
    dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]


    def dfs(v, i):
        used[v[0]][v[1]] = i
        cm[i - 1] += [v]
        for x in dr:
            u = [v[0] + x[0], v[1] + x[1]]
            if a[u[0]][u[1]] == 0 and used[u[0]][u[1]] == 0:
                dfs(u, i)


    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    a = [list(map(int, list(input()))) + [1] for i in range(n)]
    used = [[0] * n for i in range(n)]
    cm = [[], []]
    a += [[1] * n]
    s[0] -= 1
    s[1] -= 1
    f[0] -= 1
    f[1] -= 1
    dfs(s, 1)
    if used[f[0]][f[1]] == 1:
        print(0)
        return
    dfs(f, 2)
    ans = 10000
    for p1 in cm[0]:
        for p2 in cm[1]:
            ans = min(ans, (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    print(ans)


thread = threading.Thread(target=main)
thread.start()
