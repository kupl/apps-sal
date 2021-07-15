from collections import defaultdict
import sys, threading
sys.setrecursionlimit(10**8)
def inpl(k=0): return [int(x)+k for x in sys.stdin.readline().split()]

visited = [False]*(200100)
lines = defaultdict(set)

def dfs(s):
    nonlocal visited
    visited[s] = True
    ret = s
    for t in lines[s]:
        if visited[t] == False:
            ret = max(dfs(t), ret)
    return ret

def main():
    nonlocal visited
    N,M = inpl()
    for _ in range(M):
        x,y = inpl(-1)
        lines[x].add(y)
        lines[y].add(x)
    maxr = 0
    ans = 0
    for l in range(N):
        if visited[l] == False:
            r = dfs(l)
            if l < maxr:
                ans += 1
            maxr = max(r,maxr)

    print(ans)


def __starting_point():
    threading.stack_size(1024 * 100000)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()

__starting_point()
