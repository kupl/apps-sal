from collections import Counter
n = int(input())
v = list(map(int ,input().split()))

o = Counter(v[::2]).most_common() # 偶数列の最頻値の順に並べる
e = Counter(v[1::2]).most_common() # 奇数列の最頻値の順に並べる

if o[0][0] == e[0][0]: # 最頻値が偶数列と奇数列で同じかどうか判定
  if len(o) == 1: print(n//2) # 値のバリエーションが最頻値のみの場合は片方の数列を書き換えて終わり
  else:
    # 最終的に数列上に残る値の種類は2種類のみの為、上位2種の値へ全て揃える
    # 下記の2パターンで書き換える数が少ない方が回答になる
    o1,o2 = e[0][1], e[1][1]
    e1,e2 = o[0][1], o[1][1]
    
    ans = min(n-e1-o2, n-e2-o1)
    print(ans)
else:
  print(n - o[0][1] - e[0][1]) #最頻値が異なる場合は、全体の数からそれぞれの最頻値の数を引く
