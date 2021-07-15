n = int(input())
c = list(map(int, input().split()))
count = 0
while True:
    maxx = c[0]
    point = 0
    for i in range(len(c)):
        if c[i] >= maxx:
            maxx = c[i]
            point = i
    if point != 0:
        c[0] += 1
        c[point] -= 1
        count += 1
    else:
        break
print(count)
