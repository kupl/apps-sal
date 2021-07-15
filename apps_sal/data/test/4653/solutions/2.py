import sys
input = sys.stdin.readline

t=int(input())
for test in range(t):
    n,k=list(map(int,input().split()))

    if n%k>k//2:
        n-=(n%k)-k//2

    print(n)


