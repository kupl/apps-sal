n = int(input())
a = [s.split(')')[::-1] for s in input().split('(')]
x, y = 0, 0
for i in range(len(a)):
    if len(a[i]) == 2:
        for s in a[i][1].split('_'):
            if len(s) > 0:
                y += 1
    for s in a[i][0].split('_'):
        x = max(x, len(s))
print(x, y)
