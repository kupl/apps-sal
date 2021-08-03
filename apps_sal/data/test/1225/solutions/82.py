import math
H = int(input())

n = math.floor(math.log2(H))

ans = 0
for i in range(0, n + 1):
    ans += 2**i
print(ans)
