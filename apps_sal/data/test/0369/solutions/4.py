from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    inf = 10**9
    n, m = MI()
    s = SI()
    dp = [inf] * (n + 1)
    dp[0] = 0
    pre = [-1] * (n + 1)
    q = deque()
    q.append((0, 0))
    for i, c in enumerate(s[1:]):
        if q[0][0] == i - m: q.popleft()
        if c == "0":
            dp[i + 1] = q[0][1] + 1
            pre[i + 1] = q[0][0]
        while q and q[-1][1] > dp[i + 1]: q.pop()
        q.append((i + 1, dp[i + 1]))
    if dp[-1] >= inf: print(-1)
    else:
        ans = []
        now = n
        while n:
            ans.append(n - pre[n])
            n = pre[n]
        print(*ans[::-1])


main()
