n, k, q = map(int,input().split())
ans = [k-q]*n

for i in range(q):
  a = int(input())-1
  ans[a] += 1
  
for j in ans:
  if j > 0:
    print("Yes")
  else:
    print("No")
