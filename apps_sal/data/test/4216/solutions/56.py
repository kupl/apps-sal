import math
N=int(input())
root_N=int(math.sqrt(N))
for i in range(root_N,0,-1):
  if N%i==0:
    print(len(str(N//i)))
    break
