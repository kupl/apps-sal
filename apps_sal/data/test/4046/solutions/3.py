import sys
input = sys.stdin.readline
n = int(input())
Q = list(map(int, input().split()))
P = [0]
for q in Q:
    P.append(P[-1] + q)
MIN = min(P)
P2 = [p + 1 - MIN for p in P]
P3 = sorted(P2)
if P3 == list(range(1, n + 1)):
    print(*P2)
else:
    print(-1)
