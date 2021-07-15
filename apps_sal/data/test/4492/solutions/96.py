def solve():
  ans = 0
  N, x = map(int, input().split())
  A = [0]+list(map(int, input().split()))
  for i in range(1,N+1):
    if A[i]+A[i-1]>x:
      ans += A[i]+A[i-1]-x
      A[i] = x - A[i-1]
  return ans
print(solve())
