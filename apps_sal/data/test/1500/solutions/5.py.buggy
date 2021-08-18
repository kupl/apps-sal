n, k = map(int, input().split())
coords = []
for i in map(int, input().split()):
    coords.append(i)

cur = 0
count = 0
while cur != len(coords) - 1 and len(coords):
    #next_coord = coords.pop(0)
    val = coords[cur] + k
    if val < coords[cur + 1]:
        print('-1')
        return
    while cur < len(coords) and val > coords[cur]:
        cur += 1
    if cur >= len(coords) or coords[cur] > val:
        cur -= 1
    count += 1
print(count)
