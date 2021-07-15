import sys
readline = sys.stdin.readline

N = int(readline())
P = list(map(int,readline().split()))

# P[i] > P[i + 1]となっているところを交換するのを繰り返す

# 交換できるキーの集合
# 交換できないキーの集合
# を持つ
# 交換できるキーの集合を一つ見て、交換する
# 交換した結果i - 1, i + 1がそれぞれ交換可能かを確認する
# 交換可能かどうかの結果が変わっていたら、集合間で移動を行う
# 全てのキーが使用されて且つPが昇順になっていたら成功

can = set()
can_not = set()
done = set()
ans = []
for i in range(N - 1):
  if P[i] > P[i + 1]:
    can.add(i)
  else:
    can_not.add(i)

for i in range(N - 1):
  if len(can) == 0: # 所要回数の交換ができない
    print(-1)
    return
  i = can.pop() # 要素を取り出し
  P[i], P[i + 1] = P[i + 1], P[i] # 交換する
  ans.append(i)
  done.add(i)
  # この結果、i - 1とiが交換可能になっているかを確認する
  if i - 1 >= 0 and i - 1 not in done:
    if P[i - 1] > P[i]:
      if i - 1 not in can:
        can.add(i - 1)
        can_not.remove(i - 1)
    else:
      if i - 1 in can:
        can.remove(i - 1)
        can_not.add(i - 1)
  if i + 2 < N and i + 1 not in done:
    if P[i + 1] > P[i + 2]:
      if i + 1 not in can:
        can.add(i + 1)
        can_not.remove(i + 1)
    else:
      if i + 1 in can:
        can.remove(i + 1)
        can_not.add(i + 1)
        
# 所要回数の交換が実施されたので、この時点でPが昇順になっているかを確認
for i in range(N - 1):
  if P[i] > P[i + 1]:
    print(-1)
    return
    
for a in ans:
  print(a + 1)
