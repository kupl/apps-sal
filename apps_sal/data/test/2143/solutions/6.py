import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

#A.sort()

B=[]
for i in range(n-1):
    for j in range(i+1,n):
        B.append(A[i]+A[j])
        
from collections import Counter
C=Counter(B)

print(max(C.values()))

