import sys
import heapq as hq

readline = sys.stdin.readline


def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return list(map(int, readline().split()))
def nl(): return list(map(int, readline().split()))


def solve():
    s = ns()
    d = dict()
    cnt = 0
    g = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cur = (0, 0)
    d[cur] = ''
    for x in s:
        for i in range(4):
            if x == 'NEWS'[i]:
                nx = (cur[0] + g[i][0], cur[1] + g[i][1])
                if nx in d and x in d[cur]:
                    cnt += 1
                else:
                    cnt += 5
                    if nx not in d:
                        d[nx] = ''
                    d[nx] += 'NEWS'[3 - i]
                    d[cur] += x
                cur = nx
                break
    print(cnt)


T = ni()
for _ in range(T):
    solve()
