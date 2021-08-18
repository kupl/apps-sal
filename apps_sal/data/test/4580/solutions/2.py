n = int(input())
a = list(map(int, input().split()))

color = []
free = 0
Sans, Mans = 0, 0
for i in a:
    if i // 400 < 8 and i // 400 not in color:
        color.append(i // 400)
        Sans += 1
    elif i >= 3200:
        free += 1


Mans = Sans + free
if Sans == 0:
    Sans = 1
print(Sans, Mans)
