(n, m) = map(int, input().split())
distances_map = {}
num_distances = 0
for i in range(n):
    line = input()
    indexG = 0
    indexS = 0
    for j in range(len(line)):
        if line[j] == 'G':
            indexG = j
        elif line[j] == 'S':
            indexS = j
    dist = indexS - indexG
    if dist < 0:
        num_distances = -1
        break
    elif dist not in distances_map:
        distances_map[dist] = 1
        num_distances += 1
print(num_distances)
