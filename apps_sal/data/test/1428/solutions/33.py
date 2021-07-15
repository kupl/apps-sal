# 目指すグリッドは
# ABCABCABC..
# BCABCABCA..
# CABCABCAB..
# ABCABCABC..
# ...
# N = 500なので総マス数は250000
# 色の種類は30種類
# すべてのマスをあまりごとに3グループに分ける
# 各グループにおいて、各色が何マスずつあるかを計算する。250000回
# 長さ30の配列 * 3になるのであとは変更先の色をすべて試す。30 * 3回
# 隣あったマスを同じ色にすることができないため、
# グループごとに候補を3位まで用意し、3 * 2 * 1は6通りをすべて試す。
# 3位と4位がタイのときはどっちを取っても大丈夫

N,C = list(map(int,input().split()))

D = [[0]*C for i in range(C)] # 違和感
for i in range(C):
  D[i] = list(map(int,input().split())) # 色は0-indexで指定
  # D[i][j]で、iをjに変えるときの違和感を算出

# print(D)

groups = [[0]*C for i in range(3)]

for i in range(N):
  line = list(map(int,input().split()))
  for j in range(len(line)):
    groups[(i+j)%3][line[j] - 1] += 1

# groups[i(グループ名)][j(色 0-index)] = 該当する個数 が出来た。
# 各グループに対して、各色に塗り替えたときの違和感を計算する
pattern = [[[0]*2 for j in range(C)] for i in range(3)]
# pattern[i(グループ名)][j(色 0-index))] = 対象の色に塗り替えたときの違和感
# 30 * 30 = 900, 900 * 3 = 2700

for i in range(len(groups)):
  # グループごとのループ
  for j in range(C):
    # 変更後の色j
    iwakan = 0 # 色jに変えるときの違和感を累積
    for k in range(len(groups[i])):
      # グループiには色kがいくつあるか
      iwakan += groups[i][k] * D[k][j]
    pattern[i][j][0] = iwakan
    pattern[i][j][1] = j # あとで並び替えるため、何色に変えるかをメモしておく

for i in range(len(pattern)):
#  print("bef",pattern[i])
  pattern[i] = sorted(pattern[i],key = lambda x:x[0])
#  print("after",pattern[i])

ans = 10 ** 9 + 7
for a in range(3): # グループ1が何位の数字を使うか
  for b in range(3): # 同2
    if pattern[0][a][1] == pattern[1][b][1]:
      continue
    for c in range(3): # 同3
      if pattern[0][a][1] == pattern[2][c][1]:
        continue
      if pattern[1][b][1] == pattern[2][c][1]:
        continue
      val = pattern[0][a][0] + pattern[1][b][0] + pattern[2][c][0]
      if val < ans:
        ans = val
print(ans)
    

