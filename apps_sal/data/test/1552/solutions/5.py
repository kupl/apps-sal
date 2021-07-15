n=int(input())
t=list(map(int,input().split()))
C=[t.count(i) for i in range(1,4)]
print(min(C))
a=b=c=0
for _ in range(0, min(C)):
  while t[a] != 1: a += 1
  while t[b] != 2: b += 1
  while t[c] != 3: c += 1
  a += 1
  b += 1
  c += 1
  print(a, b, c)
  

