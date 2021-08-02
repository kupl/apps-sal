import threading
from sys import setrecursionlimit, exc_info


def main():
    try:
        n = int(input())
        par = list(map(int, input().split()))

        gr = [[] for i in range(n)]
        for i in range(n - 1):
            gr[par[i] - 1].append(i + 1)

        cnt = [0] * n

        def dfs(v, depth=0):
            cnt[depth] += 1
            while depth >= len(cnt):
                pass
            for u in gr[v]:
                dfs(u, depth + 1)

        dfs(0)
        print(sum([x % 2 for x in cnt]))
    except:
        print(exc_info()[0])


setrecursionlimit(100000000)
threading.stack_size(102400000)
thread = threading.Thread(target=main)
thread.start()
