N=int(input())
*A,=sorted(map(int,input().split()))

def f(x):
 for i in range(x,N,2):
  if A[i-1]!=i or A[i]!=i:
    return 0
 return 1   
    
a=1
if N%2==0:a=f(1)
else:
 if A[0]!=0:a=0
 else:a=f(2)
print(2**(N//2)%(10**9+7)*a)
