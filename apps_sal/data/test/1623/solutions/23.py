import sys
input = sys.stdin.readline

n,l,r=list(map(int,input().split()))

ANS0=(1<<l)-1+(n-l)

ANS1=(1<<r)-1+(n-r)*(1<<(r-1))

print(ANS0,ANS1)

