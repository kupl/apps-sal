import math
n, k = list(map(int, input().split()))
List = list(map(int, input().split()))
ans = math.ceil((n - 1) / (k - 1))
print(ans)
