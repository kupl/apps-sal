def seconds(l):
    time = 0
    h = 0
    for i in range(len(l) - 1):
        if h < l[i]:
            time += l[i] - h
            h += l[i] - h

        time += 1

        if h > l[i + 1]:
            time += h - l[i + 1]
            h -= h - l[i + 1]

        time += 1

    if h < l[-1]:
        time += l[-1] - h
        h += l[-1] - h
    time += 1

    return time


m = int(input())
l = []
for i in range(m):
    l.append(int(input()))
print(seconds(l))
