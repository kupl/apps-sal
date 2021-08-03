import threading
import sys


def main():
    dfs(1, cat_in[1])
    print(ans)


def dfs(v, c):
    nonlocal ans
    used[v] = True
    if cat_in[v]:
        if c > m:
            return
    else:
        c = 0
    q = 0

    for x in arr[v]:
        if not used[x]:
            dfs(x, c + cat_in[x])
            q += 1
    if q == 0 and v != 1:
        ans += 1


n, m = list(map(int, input().split()))
cat_in = [0] + [int(x) for x in input().split()]
arr = [set() for x in range(n + 1)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    arr[a].add(b)
    arr[b].add(a)
used = [False] * (n + 1)
ans = 0
sys.setrecursionlimit(10**8)
threading.stack_size(25 * 10**6)
thread = threading.Thread(target=main)
thread.start()

# main()
