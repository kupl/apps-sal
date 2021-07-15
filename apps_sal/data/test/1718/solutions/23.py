import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
min_a = min(A)
c = A.count(min_a)
ans = math.ceil((N-c)/(K-1))
print(ans)
