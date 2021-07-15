from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

import threading
threading.stack_size(67108864)
 
def main():
    n, k = list(map(int, input().split()))
    uw = []
    ubw = []
    for i in range(n):
        uw.append([])
        ubw.append([])
    for i in range(n - 1):
        a, b, v = list(map(int, input().split()))
        ubw[a - 1].append(b - 1)
        ubw[b - 1].append(a - 1)
        if v == 0:
            uw[a - 1].append(b - 1)
            uw[b - 1].append(a - 1)
    def dfs(v):
        use[v] = 1
        com[c] += 1
        for i in uw[v]:
            if not use[i]:
                dfs(i)
    use = [0] * n
    c = 0
    com = []
    for i in range(n):
        if not use[i]:
            com.append(0)
            dfs(i)
            c += 1
    q = 10 ** 9 + 7
    ans = pow(n, k, q)
    for i in range(c):
        ans -= pow(com[i], k, q)
        ans %= q
    print(ans)
thread = threading.Thread(target=main)
thread.start()
thread.join()


