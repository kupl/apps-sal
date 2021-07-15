a,b = input().split()
n,m = map(int, input().split())
s = input()
if a == s:
  print(n-1,m)
else:
  print(n,m-1)
