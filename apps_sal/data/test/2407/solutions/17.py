import heapq
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def solve():
    N, R = list(map(int, input().split()))
    M = list(set([-int(x) for x in input().split()]))
    heapq.heapify(M)

    ans = 0
    cur_pos = 0
    while M:
        cur_vanish = -heapq.heappop(M)
        if cur_vanish > cur_pos:
            cur_pos += R
            ans += 1
        else:
            break
    print(ans)


N = int(input())
for _ in range(N):
    solve()
