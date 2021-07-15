A=list(map(int,input().split()))
A.sort()
if A[-1]==sum(A[:-1]) or (A[0]+A[-1])*2==sum(A):
  print("Yes")
else:
  print("No")
