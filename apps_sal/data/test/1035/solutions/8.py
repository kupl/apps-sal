import math
ab = [int(i) for i in input().split()]
ab = math.gcd(ab[0], ab[1])
dic = {}
n = 2
while n**2 <= ab:
  if ab % n:
    n += 1
  else:
    ab //= n
    dic[n] = dic.get(n,0) + 1
if 1 < ab:
  dic[ab] = dic.get(ab,0) + 1

print(len(dic) + 1)
