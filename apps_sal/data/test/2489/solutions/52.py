import collections
n = int(input())
line = list(map(int, input().split( )))
arr = sorted(line)
coll = collections.Counter(arr)
#最大値
Ma = arr[-1]
#ソートしたn番目のやつの判定はn+1以降でおっけい. 
#同じ数字がある敵は無視
s = set()
for i in range(n):
  if coll[arr[i]] >= 2:
    s.add(arr[i])
  for j in range(2, Ma//arr[i]+1):
    s.add(arr[i]*j)
cnt = 0

#print(s)
for a in arr:
  if a in s: continue
  cnt += 1
print(cnt)
