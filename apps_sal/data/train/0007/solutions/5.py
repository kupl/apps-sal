import sys
import heapq as hq

readline = sys.stdin.readline
read = sys.stdin.read
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


def solve():
    n = ni()
    vot = [tuple(nm()) for _ in range(n)]
    vot.sort(key=lambda x: (-x[0], x[1]))
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


T = ni()
for _ in range(T):
    solve()
