# 約分して、互いに素な(1,3) (3,1)のようなペアを作りカウントする
# 正のグループと負のグループを別々に管理
# 正のグループの相手が負のグループに存在した場合、
# どちらかのグループから好きなだけ選ぶか、どちらも選ばないかしかない
# 誰ともペアにならなかったグループの個数を全て足してP個だとして、2^P通りを掛ける
# (0,0)については、その中から1つ選ぶか、選ばないかしかない

import sys
readline = sys.stdin.readline

N = int(readline())
import math

zeropair = 0
zeroa = 0
zerob = 0
from collections import defaultdict
pluspair = defaultdict(int)
minuspair = defaultdict(int)
for i in range(N):
  a,b = map(int,readline().split())
  if a == 0 and b == 0:
    zeropair += 1
    continue
  if a == 0:
    zeroa += 1
    continue
  if b == 0:
    zerob += 1
    continue
  absa = abs(a)
  absb = abs(b)
  g = math.gcd(absa,absb)
  absa,absb = absa//g,absb//g
  if a * b > 0:
    pluspair[(absa,absb)] += 1
  else:
    minuspair[(absa,absb)] += 1

DIV = 1000000007
ans = 1
# zeroa,zerobから選ぶパターンは、どちらから好きなだけ選ぶか、どちらも選ばないか
ans *= (pow(2,zeroa,DIV) + pow(2,zerob,DIV) - 1) % DIV
ans %= DIV

# 誰とでもペアになれるものをカウント
allcnt = 0

# plusから選ぶパターンで、minusにある対応ペアを探す
for item in pluspair.items():
  a,b = item[0]
  cnt = item[1]
  if (b,a) in minuspair:
    ans *= (pow(2,cnt,DIV) + pow(2,minuspair[(b,a)]) - 1) % DIV
    ans %= DIV
    del minuspair[(b,a)]
  else:
    allcnt += cnt

for val in minuspair.values():
  allcnt += val

ans = (ans * pow(2,allcnt,DIV)) % DIV
# zeropairから選んだ場合、今までのパターンとは独立
ans += zeropair
print((ans - 1) % DIV)
