n = int(input())

data = []
for j in range(n):
    data.append([int(i) for i in input().split()])

s = 1000 * 1000 * 1000 + 1
for h in range(1, 1001):
    w = 0
    ok = True
    for i in data:
        h1 = max(i[0], i[1])
        w1 = min(i[0], i[1])
        if w1 > h:
            ok = False
            break
        if h1 > h:
            w += h1
        else:
            w += w1

    if ok:
        s = min(s, h * w)

print(s)


# Made By Mostafa_Khaled
