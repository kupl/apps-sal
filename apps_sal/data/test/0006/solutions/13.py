from math import ceil
for t in range(int(input())):
    a = []
    n, x = list(map(int, input().split()))
    for i in range(n):
        a.append(list(map(int, input().split())))
    max_di = a[0][0]
    max_damage = a[0][0] - a[0][1]
    for i in a:
        if i[0] > max_di:
            max_di = i[0]
        if i[0] - i[1] > max_damage:
            max_damage = i[0] - i[1]
    x -= max_di
    if x > 0:
        if max_damage <= 0:
            print(-1)
        else:
            print(ceil(x / max_damage) + 1)
    else:
        print(1)
