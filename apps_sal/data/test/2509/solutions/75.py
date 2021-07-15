N, K = list(map(int, input().split()))

cnt = 0
for i in range(K + 1, N + 1):#b = K + 1 ... N
  k = int(N / i)
  l = N % i
  if K == 0:
    cnt += k * (i - K) + max(0, l - K)
  else:
    cnt += k * (i - K) + max(0, l - K + 1)
  #print(cnt, k, l)
  
print(cnt)  

