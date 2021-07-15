import sys
import copy
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
b = [0]
for i in range(N):
    b.append(A[i])
b.append(0)

sumb= 0
for i in range(1,len(b)):
    sumb += abs(b[i]-b[i-1])

for j in range(1,N+1):
    sumc = sumb
    sumc = sumc - abs(b[j+1]-b[j])-abs(b[j]-b[j-1])+abs(b[j+1]-b[j-1])
    print(sumc)


