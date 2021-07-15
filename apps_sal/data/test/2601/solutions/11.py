import sys
input = sys.stdin.readline

t=int(input())

for tests in range(t):
    n=int(input())
    A=list(map(int,input().split()))

    for i in range(1,n):
        if A[i-1]>A[i]:
            continue
        else:
            print("YES")
            break
    else:
        print("NO")

