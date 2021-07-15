# cook your dish here
for _ in range(int(input())):
 n,b=list(map(int,input().split()))
 ans=n-n//b
 if b==1:
  print(1)
 elif n%b:
  print(ans)
 else:
  print(ans+1)
