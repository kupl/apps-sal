N, K = map(int, input().split())
H = list(map(int, input().split()))
 
# N<=Kの場合、全てのモンスターを必殺技で倒して終了
# N>Kの場合、N体のモンスターのうち、体力が高い順に、K体を必殺技で倒す
# 残ったモンスターは、攻撃によって倒す
# 攻撃の回数を求める（必殺技は数えない）ことに注意する

# 計算量はO(NlogN)で間に合う
H = sorted(H, reverse=True)
ans = 0
if N > K: ans = sum(H[K:])
  
print(ans)
