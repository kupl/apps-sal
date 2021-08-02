import math
n, d = list(map(int, input().strip().split()))
cords = []
while n:
    cords.append(list(map(int, input().strip().split())))
    n -= 1
ans = 0
for c in cords:
    ans += 1 if math.sqrt((c[0]**2) + (c[1]**2)) <= d else 0
print(ans)
