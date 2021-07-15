def factrial(n): # 試し割り算法で素因数分解
  factors = []
  while n%2 == 0:
    factors.append(2)
    n //= 2
    
  for i in range(3, int(n**0.5)+1):
    while n%i == 0:
      factors.append(i)
      n //= i
      
  if n != 1: factors.append(n)
  
  return factors


n = int(input())
mod = 10**9+7

d = {}
for i in range(1, n+1): # 1〜nまでの各値を素因数分解
  fac = factrial(i)
  for j in fac: # 分解して取得した要素の回数をカウント
    if j in d: d[j] += 1
    else: d[j] = 1

ans = 1
for k,v in d.items():
  # 取得した要素に1を足した値を合計値にかけ合わせる
  # 約数として"1"はカウントされていない為、このタイミングで追加する
  ans *= (v+1) 
  ans %= mod
print(ans)
