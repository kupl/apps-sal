import sys
readline = sys.stdin.readline

N,A,B = list(map(int,readline().split()))
V = list(map(int,readline().split()))

# 大きいほうからA個選んだときの平均値が求める平均値
# 大きいほうからA位の数字をPとすると、
# ・A位までの数字がすべてPのとき：Pの個数から、A～B個選ぶ場合の数
# ・そうでないとき：Pの個数から、A位までに必要なPの個数を選ぶ場合の数

V = sorted(V, reverse = True)

print((sum(V[:A]) / A))

from scipy.special import comb

P = V[A - 1]
pcnt = V.count(P)

if V[0] == P:
  ans = 0
  for i in range(A, B + 1):
    ans += comb(pcnt, i, exact = True)
  print(ans)
else:
  pneed = (V[:A]).count(P)
  print((comb(pcnt, pneed, exact = True)))

