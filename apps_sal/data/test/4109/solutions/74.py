N,M,X = map(int,input().split())
array = [ list(map(int,input().split())) for _ in range(N) ]
ans = 10**18
for i in range ( 2**N ):
  price = 0
  skill = [0]*M
  count = 0
  for k in range(N):
    if ( i >> k ) & 1:
      price += array[k][0]
      for j in range (M):
        skill[j] += array[k][j+1]
  for t in range(M):
    if skill[t] < X:
      break
    else:
      count += 1
    if count == M:
      ans = min(price,ans)
      
print( -1 if ans == 10**18 else ans)
