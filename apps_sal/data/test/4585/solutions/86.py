s=int(input())
n=1
s2=0
while True:
  s2=n*(n+1)//2
  if s2>=s:
    print(n)
    break
  else:
    n=n+1
