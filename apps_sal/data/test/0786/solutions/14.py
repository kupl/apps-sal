n = int(input())
up = 0
wasup = 0
down = 0
wasdown = 0
for i in range(n):
    c, d = [int(i) for i in input().split()]
    if d == 1:
        if not wasdown:
            down = 1900
            wasdown = 1
        down = max(down, 1900)
        down+=c
        if wasup:
            up+=c

    if d == 2:
        if not wasup:
            up = 1899
            wasup = 1
        up = min(up, 1899)
        up+=c
        if wasdown:
            down+=c
    if wasup and wasdown:
        if up<down:
            print("Impossible")
            break
else:
    if wasup:
        print(up)
    else:
        print("Infinity")
