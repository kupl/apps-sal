import math
n, h = map(int, input().split())
katana = []
a_max = 0

for i in range(n):
    ab = list(map(int, input().split()))
    katana.append(ab)
    a_max = max(a_max, ab[0])

katana = sorted(katana, key=lambda x: x[1], reverse=True)
life = h
count = 0
for a, b in katana:
    if b <= a_max:
        break
    else:
        life -= b

    count += 1
    if life <= 0:
        break

if life > 0:
    count += math.ceil(life / a_max)

print(count)
