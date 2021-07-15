M, K = map(int, input().split())

#K と K の間で K を作れれば、数列は存在する。  
#絶対に作れないパターン
if K >= 2 ** M:
  print("-1")
  return
if M == 0:
  print(0, 0)
  return
elif M == 1:
  if K == 0:
    print(0, 0, 1, 1)
  else:
    print(-1)
  return
#K と K の間で K を作れれば、数列は存在する。  
  
now = 0  
for i in range(2 ** M):
  if i != K:
    now = now^i
  #print(now)
#print(now)

print(K, end = " ")
for i in range(2 ** M):
  if i != K:
    print(i, end = " ")
print(K, end = " ")
for i in range(2 ** M):
  if (2 ** M - 1 - i) != K:
    print(2 ** M - 1 - i, end = " ")
  
  
  

  
  
