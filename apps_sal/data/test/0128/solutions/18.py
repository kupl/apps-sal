import math
data = input()
n, k = data.split(' ')

n = int(n)
k = int(k)
m = n
chaos = 0
for i in range(k):
    if i < math.floor(n/2):
        chaos += 2*m - 3
        m -= 2
    else:
        break
print(chaos)
