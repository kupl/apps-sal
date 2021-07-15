import sys
input = sys.stdin.readline

t=int(input())
for test in range(t):
    h,w=list(map(int,input().split()))

    print(24*60-h*60-w)


