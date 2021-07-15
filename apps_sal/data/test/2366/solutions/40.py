N = int(input())
A = list(map(int, input().split()))
di = {}

for a in A:
  if a not in di.keys(): # diに何もなかった場合
    #print("add")
    di[a] = 1
  else:
    #print("sum")
    di[a] += 1

# 全体量計算
sum = 0
for a, b in di.items():
  #print(a,b)
  sum += int((b*(b-1))/2*1)
  
# 組み合わせ計算
for k in A:
  n = di[k]
  bef = n*(n-1)/2
  aft = (n-1)*(n-2)/2
  print(int(sum-bef+aft))
