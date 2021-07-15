import sys
import heapq as hq

readline = sys.stdin.readline
read = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    n = ni()
    vot = [tuple(nm()) for _ in range(n)]
    vot.sort(key = lambda x: (-x[0], x[1]))
    q = list()
    c = 0
    cost = 0
    for i in range(n):
        hq.heappush(q, vot[i][1])
        while n - i - 1 + c < vot[i][0]:
            cost += hq.heappop(q)
            c += 1
    print(cost)
    return


# solve()

T = ni()
for _ in range(T):
    solve()

