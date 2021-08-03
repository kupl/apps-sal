x, y = map(int, input().split())

tower = []
for i in range(1, 1000):
    tower.append(i * (i + 1) / 2)

for n in range(0, 998):
    if tower[n] - x == tower[n + 1] - y:
        print(int(tower[n] - x))
