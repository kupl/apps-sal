DIR = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}

for t in range(int(input())):
    path = input()
    tracks = set()
    x, y = 0, 0
    time = 0
    for char in path:
        x1 = x + DIR[char][0]
        y1 = y + DIR[char][1]
        if (x, y, x1, y1) in tracks or (x1, y1, x, y) in tracks:
            time += 1
        else:
            time += 5
            tracks.add((x, y, x1, y1))
        x, y = x1, y1
    print(time)
