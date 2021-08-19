import sys
sys.setrecursionlimit(2147483647)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    k = int(input())
    score = 0
    B = 0
    from heapq import heappush, heappop
    q = []
    Q = []
    for _ in range(k):
        s = input()
        if s[0] == '1':
            (s, a, b) = map(int, s.split())
            heappush(q, -a)
            heappush(Q, a)
            B += b
            t = -q[0]
            T = Q[0]
            if t > T:
                score += t - T
                heappop(q)
                heappop(Q)
                heappush(q, -T)
                heappush(Q, t)
        else:
            print(-q[0], score + B)


resolve()
