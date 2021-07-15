def solve():
  N = int(input())
  A = list(map(int, input().split()))
  B = [abs(a) for a in A]
  ans = sum(B)
  under = [a for a in A if a<0]
  if len(under)%2==1:
    ans -= min(B)*2
  return ans
print(solve())
