line = input().split()
h1 = int(line[0])
h2 = int(line[1])
line = input().split()
a = int(line[0])
b = int(line[1])
if a <= b:
    if h1 + 8 * a >= h2:
        print(0)
    else:
        print(-1)
else:
    slips = 0
    while True:
        if h1 + 8 * a + slips * 12 * (a - b) >= h2:
            print(slips)
            break
        slips += 1
