N,X = map(int,input().split())

# レベル0バーガー P
# レベル1バーガー BPPPB
# P[i] = レベルiバーガーのパティの枚数
# B[i] = レベルiバーガーの厚さ

P = [0] * 51
B = [0] * 51

P[0] = 1
B[0] = 1

for i in range(1, len(P)):
  P[i] = P[i - 1] * 2 + 1
  B[i] = B[i - 1] * 2 + 3

# レベルnバーガーを丸ごと食べたときのパティの枚数を求める
def get_whole_barger(n):
  return P[n]

# レベルnバーガーをx枚目まで食べたときのパティの枚数を求める
def get_patty(n,x):
  if n == 0 or x == 0:
    return P[0]
  if B[n] == x:
    return P[n]
  if x <= 1:
    return 0
  if x <= 1 + B[n - 1]:
    return get_patty(n - 1, x - 1)
  if x <= 2 + B[n - 1]:
    return get_whole_barger(n - 1) + 1
  if x <= 2 + B[n - 1] * 2:
    return get_whole_barger(n - 1) + 1 + get_patty(n - 1, x - 2 - B[n - 1])
  else:
    return get_whole_barger(n - 1) + 1 + get_whole_barger(n - 1)

print(get_patty(N,X))
