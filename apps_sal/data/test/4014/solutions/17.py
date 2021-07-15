a = input().split(" ")
a = [int(e) for e in a]

isdc = []
for i in range(a[1]):
    l = input().split(" ")
    l = [int(e) for e in l]
    isdc.append([i+1, l[0]-1, l[1]-1, l[2]])

l = [0] * a[0]
for e in isdc:
    l[e[2]] = len(isdc) + 1

isdc = sorted(isdc, key=lambda one: one[2])

for exam in isdc:
    day = exam[1]
    while day < exam[2]:
        if exam[3] == 0:
            break
        if l[day] == 0:
            l[day] = exam[0]
            exam[3] -= 1

        day += 1

    if exam[3] != 0:
        print(-1)
        return

for e in l:
    print(e, end=" ")

