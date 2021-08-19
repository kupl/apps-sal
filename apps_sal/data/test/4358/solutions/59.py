import math
N = int(input())
p = []
for i in range(N):
    p.append(int(input()))
total_price = max(p) / 2 + sum(p) - max(p)
print(math.floor(total_price))
