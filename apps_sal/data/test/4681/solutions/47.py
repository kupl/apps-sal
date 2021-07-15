n=int(input())
a=2
b=1
i=0
while i<n:
  d=a
  a=b
  b=d+b
  i=i+1
print(a)
