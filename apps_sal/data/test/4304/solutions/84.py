a, b = map(int, input().split())

tower_height = 0
tower_height_list = []
for i in range(1,999+1):
    tower_height += i
    tower_height_list.append(tower_height)
    i += 1

for i in range(len(tower_height_list)):
    if tower_height_list[i] - b == tower_height_list[i-1] - a:
        print(tower_height_list[i] - b)
