t = int(input())
for i in range(t):
 #n for number of cookies and b for crumbs
 n , b = map(int,input().split(" "))
 if n == b:
  print(n)
 elif n%b == 0:
  print(n - n//b + 1)
 else:
  print(n - n//b)
