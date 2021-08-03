i = 1
angles = set()
while True:
    angle = (180 * i) / (i + 2)
    if angle > 179:
        break
    if (180 * i) % (i + 2) == 0:
        angles.add(int(angle))
    i += 1
t = int(input())
for i in range(t):
    x = int(input())
    if x in angles:
        print('YES')
    else:
        print('NO')
