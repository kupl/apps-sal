import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''


n=int(input())
a=list(map(int,input().split()))
a.sort()
#print(a)
ans=0
from math import floor
for i in range(1,n):
    ans+=a[n-1-floor(i/2)]
    #print(ans)
print(ans)

