import sys
input = sys.stdin.readline

q=int(input())

for testcases in range(q):
    n=int(input())
    A=list(map(int,input().split()))

    print(-(-sum(A)//n))

