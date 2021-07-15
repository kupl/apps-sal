from math import gcd
 
N = int(input())
mod = 10 ** 9 + 7 # 1000000007
 
d = dict()
zeros = 0
for _ in range(N):
  a, b = map(int, input().split()) # Ai, Bi
  # どちらか一方でも0であれば特殊なケースとなる
  # 下記のd[p]でd[(0, 0)]のような形になるため分ける(zeros)
  # d[(0, 0)]同士では組み合わせが作れないため、単純に+1していく
  if not any((a,b)):
    zeros += 1
    continue
  if all((a, b)):
    g = gcd(a, b) * (a//abs(a)) # //は切り捨て除算
  elif a:
    g = a
  else:
    g = b
  p = a//g, b//g # p is (tuple)
  d[p] = d.get(p, 0) + 1 # count

ans = 1 # 掛け算するため0ではなく1としておき、最後の出力時に1を引くようにする
done = set()
for (a,b), val in d.items():
  if (-b, a) in done or (b, -a) in done: # if already counted, then continue
    continue
  done.add((a, b))
  w = d.get((-b, a), 0) + d.get((b, -a), 0)
  # (a, b)とそれに垂直な(-b, a), (b, -a)のそれぞれの組み合わせを足す
  # そして何も選ばなかったときの場合を引くため、最後に-1とする
  ans *= (pow(2, val) + pow(2, w) -1)
  ans %= mod

print((ans + zeros -1) % mod)
