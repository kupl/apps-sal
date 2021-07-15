t=int(input())
for i in range(t):
  n=int(input())
  a=[int (i) for i in input().split()]
  a=sorted(a)
  print(a[n]-a[n-1])
