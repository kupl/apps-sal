def main():
  N, K = map(int, input().split())
  N = N + 1
  A=[n for n in range(N)]
  S=[0]*(N+1)
  for a in A:
    S[a+1]+=S[a]+a
  ans=0
  for k in range(K, N+1):
    maxS, minS=S[-1], S[k]
    offset=S[-k-1]
    ans+=(maxS - offset) - minS + 1
  print(ans%(1000000007))
  
def __starting_point():
  main()
__starting_point()
