from collections import Counter
 
N, K = map(int, input().split())
A = list(map(int, input().split()))
 
# N=O(10^5)なので、O(N)で解く
# ABC-155-C-Poll の類題
# 方針：各数字の出現回数を数える
 
# Counter(リスト) は辞書型のサブクラスであり、キーに要素・値に出現回数という形式
# Counter(リスト).most_common() は(要素, 出現回数)というタプルを出現回数順に並べたリスト
A = Counter(A).most_common()
 
# 出現回数の大きい方からK種類はそのままにしておく。これによって、変えない個数が求まる。
# 変える個数は、N-(変えない個数)
s = 0
for i in range(min(K, len(A))):
  s += A[i][1]
  
print(N-s)
