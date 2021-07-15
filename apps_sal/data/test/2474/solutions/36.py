def solve():
  ans = 0
  N = int(input())
  C = list(map(int, input().split()))
  C.sort()
  mod = 10**9+7
  for i in range(N):
    ans += C[i]*(N+1-i)
  ans = ans*pow(2,2*N-2)%mod
  return ans
print(solve())
