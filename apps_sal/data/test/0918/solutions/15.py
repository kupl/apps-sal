string = input().split()
n = int(string[0])
m = int(string[1])
regions = []
for i in range(m + 1):
    regions.append([])

for i in range(n):
    string = input().split()
    reg = int(string[1])
    name = string[0]
    points = int(string[2])
    regions[reg].append((name, points))

for i in range(1, m + 1):
    regions[i].sort(key=lambda x: x[1], reverse=True)
    if len(regions[i]) == 2:
        print(regions[i][0][0], regions[i][1][0])
    elif regions[i][1][1] == regions[i][2][1]:
        print('?')
    else:
        print(regions[i][0][0], regions[i][1][0])
