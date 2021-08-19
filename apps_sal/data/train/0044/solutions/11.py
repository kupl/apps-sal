import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # N,K=map(int,input().split())
    # A=list(map(int,input().split()))
    n = int(input())
    v = 4 * n
    for i in range(n):
        print(v, end=" ")
        v = v - 2
    print()
