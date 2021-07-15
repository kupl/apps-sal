from bisect import bisect_left,bisect_right
a=[1]
f=1
while a[-1]<=10**18:
  f=f*2+1
  a.append(a[-1]+f*(f+1)//2)
for _ in range(int(input())):
  n=int(input())
  print(bisect_right(a,n))
