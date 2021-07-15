m = int(input())
col = 0
pos = 0
a1 = -1
a2 = -1
while True:
    pos += 1
    h = 1
    e = 0
    while pos % (5 * h) == 0:
        h *= 5
        e += 1
    col += e
    if a1 == -1 and col == m:
        a1 = pos
    if col > m:
        a2 = pos
        break
if a1 > 0 and a2 > 0:
    print(a2 - a1)
    for i in range(a1, a2):
        print(i, end = ' ')
else:
    print(0)
    
    

