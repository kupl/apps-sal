import math

N = int(input())
V = [int(input()) for _ in range(5)]

latest = min(V)
ans = math.ceil(N / latest) + 4
print(ans)
