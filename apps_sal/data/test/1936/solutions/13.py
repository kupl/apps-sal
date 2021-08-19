import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    (L, R) = [int(_) for _ in input().split()]
    if R < L * 2:
        print(-1, -1)
    else:
        print(L, L * 2)
