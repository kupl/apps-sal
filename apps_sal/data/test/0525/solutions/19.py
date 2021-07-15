import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n=int(input())
    A=list(map(int,input().split()))

    if len(set(A))==1:
        print(n)
    else:
        print(1)


