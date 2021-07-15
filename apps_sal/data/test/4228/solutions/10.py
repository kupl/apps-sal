# N,Lを取得する
N, L = map(int, input().split())
# 味のリストを作成する
tastes = []
for i in range(1,N+1):
    tastes.append(L+i-1)
    
# 味の絶対値が最も小さいリストのindexを取得する
abs_tastes = list(map(abs, tastes))
min_tastes_index = abs_tastes.index(min(abs_tastes))
tastes.pop(min_tastes_index)

# 上記リンゴを除いた残りのリンゴの味の総和を求める
print(sum(tastes))
