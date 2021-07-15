N, K = map(int, input().split())
A = list(map(int, input().split()))

# N=O(10^5)なので、O(N)で解く
# ABC-155-C-Poll の類題

# 各数字の出現回数を数える
dic = {}
for i in range(N):
  a = A[i]
  if a not in dic: dic[a] = 1
  else: dic[a] += 1

# dicを昇順にソート
dic = sorted(dic.items(), key=lambda x:x[1])

# dicは [(5, 1), (3, 2), (2, 2), (4, 2), (1, 3)] のようになっている
# dicのvalueにおいて、前からlen(dic)-K個の和を取る
ans = 0
for i in range(max(len(dic)-K, 0)):
  ans += dic[i][1]
  
print(ans)
