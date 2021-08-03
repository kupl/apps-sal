import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]
    if A[0] + A[1] <= A[-1]:
        print(1, 2, N)
    else:
        print(-1)
