# cook your dish here
n,q=list(map(int,(input()).split()))
a=list(map(int,(input()).split()))
b=min(a)
c=max(a)
for i in range(q):
 t=int(input())
 if t>=b and t<=c:
  print("Yes")
 else:
  print("No")

