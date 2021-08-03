import math

n = int(input())
abc = [int(input()) for i in range(5)]

ans = 4 + math.ceil(n / min(abc))
print(ans)
