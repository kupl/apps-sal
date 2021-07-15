# Nを受け取る
N = int(input())

# Lを受け取る
L = list(map(int, input().split()))

# 組み合わせを作る
import itertools as it

c = it.combinations(L, 3)

# 3辺の長さが異なる組み合わせを作る & 長辺 < 他2辺の和
count = 0
for i in c:
  #print(i[0], i[1], i[2])
  # カウントする
  if len(set(i)) == 3:
    a,b,c = sorted(i, reverse=True)
    #print(a,b,c)
    if a < b+c:
      count+= 1
# 出力
print(count)
