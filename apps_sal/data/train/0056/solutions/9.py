import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    m=k//n
    r=k%n
    if r:
        print(2)
        s='1'*(m+1)+'0'*(n-m-1)
        for i in range(r):
            print(s)
            s=s[1:]+s[0]
        i=(m-r)%n
        s=s[:i]+'0'+s[i+1:]
        for i in range(n-r):
            print(s)
            s=s[1:]+s[0]
    else:
        print(0)
        s='1'*m+'0'*(n-m)
        for i in range(n):
            print(s)
            s=s[1:]+s[0]
