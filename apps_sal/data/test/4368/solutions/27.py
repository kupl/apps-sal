def L():
  return list(map(int, input().split()))
import math
[n,k]=L()

print(math.floor(math.log(n,k))+1)
