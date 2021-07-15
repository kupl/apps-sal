#4 9
#1 3 5 6
#の時に1（正解は0）と出力されるがACになる

N, K = list(map(int, input().split()))
a=list(map(int, input().split()))
a.sort()
ans = N
t = 0
for i in range(N-1, -1, -1) :
  if t+a[i] < K:
    t += a[i]
  else:
    ans = min(ans, i)
print(ans)

