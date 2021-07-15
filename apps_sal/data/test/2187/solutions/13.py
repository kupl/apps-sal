import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sol=0
    for i in range(1,n):
        if a[i]<a[i-1]:
            sol+=a[i-1]
            sol-=a[i]
    print(sol)
