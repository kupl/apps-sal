import math
N = int(input())

# (1, 1)から(a, b)に至るまでの移動回数は(a+b−2)であることに注意すると、
# a*b=N を満たす(a, b)について(a+b−2)の最小値を求めればよい
# 対称性より、O(√N)
# 今回はN=O(10^12)なので間に合う

# a+b-2の最小値を求める
ans = N-1
for i in range(1, int(math.sqrt(N))+1):
  if N % i == 0:
    ans = min(ans, (N//i)+i-2)
    
print(ans)
