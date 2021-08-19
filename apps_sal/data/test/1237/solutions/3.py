import math
(n, s) = tuple(map(int, input().split()))
floors = [0 for i in range(s + 1)]
for i in range(n):
    (floor, time) = tuple(map(int, input().split()))
    floors[floor] = max(floors[floor], time)
res = s
for i in range(s + 1):
    res = max(res, floors[i] + i)
print(res)
