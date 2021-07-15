n, m = tuple(map(int, str.split(input())))
a = tuple(map(int, str.split(input())))
mi = tuple(map(int, str.split(input())))
ms = sorted([a[i - 1] for i in mi], reverse=True)

points = 0
for i, ai in enumerate(a):

    if i + 1 not in mi:

        points += ai

for m in ms:

    if m > points:

        points += m

    else:

        points += points

print(points)

