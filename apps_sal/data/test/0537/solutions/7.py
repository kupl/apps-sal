
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n,k=list(map(int,input().split()))

factor=(n//2)//(k+1)

print("%d %d %d"%(factor,factor*k,n-factor*(k+1)))

