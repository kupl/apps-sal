import sys
input = sys.stdin.readline

t=int(input())

for test in range(t):
    a,b,c,n=list(map(int,input().split()))

    M=max(a,b,c)
    n-=(M-a)+(M-b)+(M-c)

    if n<0:
        print("NO")
    else:
        if n%3==0:
            print("YES")
        else:
            print("NO")

