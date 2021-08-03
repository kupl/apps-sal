dom_color = [int(x) for x in input().split(' ')]
dom = [int(x) for x in input().split(' ')]
max1 = 1
max2 = 1
for i in range(dom_color[0] - 1):
    if dom[i] != dom[i + 1]:
        max2 += 1
    if dom[i] == dom[i + 1]:
        if max2 > max1:
            max1 = max2
        max2 = 1
if max2 > max1:
    max1 = max2
print(max1)
