import sys
input = sys.stdin.readline

t=int(input())

for testcases in range(t):
    x,y=list(map(int,input().split()))

    if x==1:
        if y==1:
            print("YES")
        else:
            print("NO")

    elif x<=3:
        if y<=3:
            print("YES")
        else:
            print("NO")

    else:
        print("YES")

