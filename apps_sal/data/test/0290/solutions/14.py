import math

n = int(input())
sq = int(math.sqrt(n))
dif = n - sq * sq
add = 0
if dif > sq:
    add = 2
elif dif != 0:
    add = 1
print(2 * sq + add)

