import statistics
n=int(input())
la, lb = [], []
for _ in range(n):
  a, b =list(map(int, input().split()))
  la.append(a)
  lb.append(b)
c=statistics.median(la)
d=statistics.median(lb)
if n%2==1:
  print((d-c+1))
else:
  print((int(2*d-2*c+1)))








