def prime_fact(N):
  M = N
  primes = []
  K = 2

  while K*K <= M:
    while N%K == 0:
      primes.append(K)
      N = N//K
    K += 1
  
  if N != 1:
    primes.append(N)

  return primes

N = int(input())
nums = [0]*1000
ans = 1

for i in range(2,N+1):
  P = prime_fact(i)
  for j in range(len(P)):
    nums[P[j]-1] += 1

for k in range(1000):
  ans = ans*(nums[k]+1)%1000000007

print(ans)
