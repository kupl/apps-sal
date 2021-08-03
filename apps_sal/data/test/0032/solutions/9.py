n = int(input())
loc = 0
for i in range(n):
    dist, direct = input().split()
    dist = int(dist)
    if (loc == 0 and direct != 'South'
            or loc == 20000 and direct != 'North'):
        print("NO")
        break
    if direct == 'South':
        loc += dist
    elif direct == 'North':
        loc -= dist
    if loc < 0 or loc > 20000:
        print("NO")
        break
else:
    print("YES" if loc == 0 else "NO")
