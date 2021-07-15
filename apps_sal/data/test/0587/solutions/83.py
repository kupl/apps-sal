# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
TD = [tuple(map(int,input().split())) for _ in range(N)]

# 美味しい順にソートしておく
#  t : ネタの種類
#  d : 美味しさ基礎ポイント
TD.sort(key=lambda x:x[1], reverse=True)

# 美味しい順にK個食べた場合の満足ポイント
ans = 0
s = set() # 食べたネタの集合
r = list() # すでに食べたネタ, あとで交換する用
for i in range(K):
    t,d = TD[i]
    ans += d
    if t not in s:
        s.add(t) # 食べたネタの種類の集合
    else:
        r.append(TD[i])
ans += len(s)**2

Ans = ans

# 美味しい順のK+1番目から, ネタの種類が増えるような操作を順番に試していく
for i in range(K,N):
    t0,d0 = TD[i]
    # まだ食べてないネタ and 交換用の寿司があるなら
    if t0 not in s and len(r) > 0:
        # 交換用の寿司の一番美味しさ基礎ポイントが低いものを交換するのが最善
        t1,d1 = r.pop()
        # 満足ポイントの再計算
        ans = ans - d1 + d0 - len(s)**2 + (len(s)+1)**2
        # 食べたネタの集合に追加
        s.add(t0)
        # 満足度が大きくなったか都度確認
        Ans = max(Ans,ans)

print(Ans)
