n=int(input())
a=list(map(int,input().split()))
odd=[]
even=[]
if n%2==0:
  m=n//2
  for i in range(m):
    odd.append(a[n-1-2*i])
    even.append(a[2*i])
  print(*(odd+even))
else:
  m=n//2
  for i in range(m):
    odd.append(a[n-1-2*i])
    even.append(a[n-2-2*i])
  even.reverse()
  odd=odd+[a[0]]
  print(*(odd+even))
