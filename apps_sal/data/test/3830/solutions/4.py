import math

T = int(input())

#lets = 'abcdefghijklmnopqrstuvwxyz'
#key = {lets[i]:i for i in range(26)}

for t in range(T):
  n = int(input())
  #x1,y1,x2,y2 = map(int,input().split())
  #a = list(map(int,input().split()))
  #a = list(input())
  a = input()
  d = False
  if a.count('>') == 0:
    print(n)
    continue
  if a.count('<') == 0:
    print(n)
    continue
  ans = 0
  for i in range(n):
    if a[i]=='-' or a[i-1]=='-':
      ans+=1
  print(ans)


