n,m = list(map(int,input().split()))
total = n*m

if n==1 and m==1:
  print((1))
  
elif n == 1 or m == 1:
  print((total - 2))

else:
  print((total - (2*(n+m-2))))
  

