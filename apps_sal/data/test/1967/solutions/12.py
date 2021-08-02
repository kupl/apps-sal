w, h = [int(x) for x in input().split(' ')]
img = []
for i in range(h):
    img.append([c for c in input()])

for j in (range(w)):
    row = []
    for i in (range(h)):
        row.append(img[i][j])
        row.append(img[i][j])
    print(*row, sep='', end='\n')
    print(*row, sep='', end='\n')
