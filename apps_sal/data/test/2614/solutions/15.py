import math

T = int(input())

for i in range(T):
  n = int(input())
  #n,p,k = map(int, input().split())
  a = list(map(int,input().split()))
  #b = list(map(int,input().split()))
  #a = input()
  d = False
  A = [0]*n
  
  for i in range(n):
    A[a[i]-1]+=1

  #A.sort(reverse=True)
  ma = max(A)
  man = A.count(ma)

  #if man == 1:
  print((n-man)//(ma-1)-1)
  #print(n,ma,man)
  

