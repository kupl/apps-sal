def solve():
  N, K = map(int, input().split())
  S = input()
  cnt = 1
  for i in range(N-1):
    if S[i]!=S[i+1]:
      cnt += 1
  ans = N-max(1,cnt-K*2)
  return ans
print(solve())
