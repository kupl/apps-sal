N, K=map(int, input().split())

if K==0:
  print(N*N)
  return
  
print(sum([(N//b)*(b-K)+max(N%b-K+1, 0) for b in range(K+1, N+1)]))
