import sys
input = sys.stdin.readline

n=int(input())
A=list(input().split())
mod= 998244353


def dup(a):
    ANS=""
    for k in a:
        ANS+=k*2

    return int(ANS)

B=[dup(a) for a in A]

ANS=0
for b in B:
    ANS=(ANS+b*n)%mod

print(ANS)

