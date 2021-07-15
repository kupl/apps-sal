import sys
stdin=sys.stdin

ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()
yp='Yes'
np='No'

s=sp()
t=sp()

l=len(s)

if s[0:l]==t[0:l]:
  print(yp)
else:
  print(np)
