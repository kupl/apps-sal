n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a = a[::-1]
s = sum(a)
if a[m-1]<s/(4*m):
  print("No")
else:
  print("Yes")
