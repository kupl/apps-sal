N, K = list(map(int, input().split()))
A = 1
ans = 0



while (A <= N):
  count = 0
  T = A
  while (T<K):
    T = T*2
    count += 1
  ans += float((1/N)*(1/2)**count)
  A += 1
  
print(ans)

