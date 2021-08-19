import math
n = int(input())
A = [int(input()) for _ in range(5)]
ans = math.ceil(n / min(A)) + 4
print(ans)
