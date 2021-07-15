import sys
input=sys.stdin.readline
q=int(input())
for _ in range(q):
  n=int(input())
  ans=0
  a,b=list(map(int,input().split()))
  cur=a
  A=[0,b,2*b]
  for i in range(n-1):
    a=cur
    na,nb=list(map(int,input().split()))
    cur=na
    a0,a1,a2=A
    if na==a:
      A[0]=min(a1,a2)
      A[1]=nb+min(a0,a2)
      A[2]=2*nb+min(a0,a1)
    elif na==a-1:
      A[0]=min(a0,a1,a2)
      A[1]=nb+min(a1,a2)
      A[2]=2*nb+min(a0,a2)
    elif na==a-2:
      A[0]=min(a0,a1,a2)
      A[1]=nb+min(a0,a1,a2)
      A[2]=2*nb+min(a1,a2)
    elif na==a+1:
      A[0]=min(a0,a2)
      A[1]=nb+min(a0,a1)
      A[2]=2*nb+min(a0,a1,a2)
    elif na==a+2:
      A[0]=min(a0,a1)
      A[1]=nb+min(a0,a1,a2)
      A[2]=2*nb+min(a0,a1,a2)
    else:
      A[0]=min(a0,a1,a2)
      A[1]=nb+min(a0,a1,a2)
      A[2]=2*nb+min(a0,a1,a2)
 
  print(min(A))

