c = n = int(input())
l = []
while c:
    a = input().split(' ')
    a = [int(i) for i in a]
    l.append((a[0], a[1]))
    c -= 1
count = 0
h = 0
while h < n:
    g = h + 1
    while g < n:
        if l[h][0] == l[g][1]:
            count += 1
        if l[h][1] == l[g][0]:
            count += 1
        g += 1
    h += 1
print(count)
