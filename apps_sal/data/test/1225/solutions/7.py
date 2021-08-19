import math
h = int(input())
atk = 0
enemy = 1
while True:
    if h > 1:
        h = math.floor(int(h / 2))
        atk += enemy
        enemy *= 2
    elif h == 1:
        atk += enemy
        break
print(atk)
