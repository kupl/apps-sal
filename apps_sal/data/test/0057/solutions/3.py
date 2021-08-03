n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))

x1, y1, x2, y2 = float('inf'), float('inf'), float('inf'), float('inf')
for i in a:
    if x1 == float('inf'):
        x1 = i[0]
    elif x2 == float('inf') and x1 != i[0]:
        x2 = i[0]

    if y1 == float('inf'):
        y1 = i[1]
    elif y2 == float('inf') and y1 != i[1]:
        y2 = i[1]

if y2 == float('inf') or x2 == float('inf'):
    print('-1')
else:
    print(abs(x1 - x2) * abs(y1 - y2))
