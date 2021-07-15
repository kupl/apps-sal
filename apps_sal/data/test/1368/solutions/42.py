import collections
from operator import mul
from functools import reduce

N,A,B = list(map(int, input().split()))
V = list(map(int, input().split()))
VV = sorted(V,reverse = True)
ave = 0
ml = []

for i in range(A,B + 1):
  avet = sum(VV[:i]) / i
  if avet >= ave:
    ml.append(i)
    ave = max(ave,avet)
  else:
    break

dic = collections.Counter(V)
#print(dic,ml)

def cmb(n,r):
  r = min(n - r,r)
  if r == 0:
    return 1
  over = reduce(mul,list(range(n, n - r, -1)))
  under = reduce(mul,list(range(1,r + 1)))
  return over // under

res = 0

for j in ml:
  r = dic[VV[j - 1]]
  rr = VV.index(VV[j - 1])
  res += cmb(r,j - rr)

print(ave)
print(res)

