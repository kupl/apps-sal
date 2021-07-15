import math
a, b = map(int,input().split())
ans = -1
for i in range(1, 1011):
  if math.floor(i*0.08) == a and math.floor(i * 0.1) == b:
    print(i)
    return
print(ans)
