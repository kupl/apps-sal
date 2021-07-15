n=int(input())

if n==1: print(0); return;
if n==2: print(1); return;

if n%2==1:
  print(((n-1)+1)*((n-1)//2))
else:
  print(((n-1)+1)*((n-1)//2)+n//2)
