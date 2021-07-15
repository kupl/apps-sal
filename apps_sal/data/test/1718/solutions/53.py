import math

n,k = map(int,input().split())
Ai = list(map(int,input().split()))
#a = Ai.index(1)

print(math.ceil((n-k) / (k-1) + 1))
