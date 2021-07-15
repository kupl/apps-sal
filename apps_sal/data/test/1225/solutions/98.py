import math
h = int(input())
l = 1

while (h != 1):
    h = math.floor(h / 2)
    l += 1
ans = 0

for i in range(l):
    ans += 2**i
print(ans)
