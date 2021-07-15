N, K = map(int, input().split())

def sigma(N, k):
  a = (k*(k+1)*(2*k+1)//6)%(10**9+7)
  b = (k*(k+1)//2)%(10**9+7)
  c = k
  return -a + (N+1)*b + c

print((sigma(N,N+1)-sigma(N, K-1))%(10**9+7))
