N=int(input())
A=[]
B=[]
for i in range(N):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
A.sort()
B.sort()
def median(x):
  l=len(x)
  if l%2==0:
    return (x[l//2-1]+x[l//2])/2
  else:
    return x[l//2]
if N%2==1:
  print(median(B)-median(A)+1)
else:
  print(int((median(B)-median(A))*2+1))
