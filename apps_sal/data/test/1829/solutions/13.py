import math

nandm = input().split()
n = int(nandm[0])
m = int(nandm[1])

poland_strings = []
for i in range(0, n):
    poland_strings += [input().strip()]

enemy_strings = []
for i in range(0, m):
    enemy_strings += [input().strip()]

common = 0.
for word in poland_strings:
    if word in enemy_strings:
        common += 1

n -= math.floor(common / 2.0)
m -= math.ceil(common / 2.0)

if n > m:
    print("YES")
else:
    print("NO")
