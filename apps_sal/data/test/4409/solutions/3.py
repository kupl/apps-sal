import sys
input = sys.stdin.readline
from collections import Counter

n=int(input())
A=list(map(int,input().split()))

counter=Counter(A)
x,y=counter.most_common(1)[0]


print(n-y)

for i in range(n):
    if A[i]==x:
        start=i
        break

for j in range(start,-1,-1):
    if A[j]==x:
        continue
    if A[j]>x:
        print(2,j+1,j+2)
    else:
        print(1,j+1,j+2)



for j in range(start,n):
    if A[j]==x:
        continue
    if A[j]>x:
        print(2,j+1,j)
    else:
        print(1,j+1,j)


