import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    K, N, A, B = map(int, input().split())
    if B*N >= K:
        print(-1)
    elif A*N < K:
        print(N)
    else:
        print(-((-(K-B*N))//(A-B))-1)
