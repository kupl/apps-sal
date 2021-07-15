import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    if p[0]>p[-1]:
        print("NO")
    else:
        print("YES")
