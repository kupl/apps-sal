import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = math.ceil((N-1)/(K-1))
print(ans)
