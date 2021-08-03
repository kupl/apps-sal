n = int(input())
array = list(map(int, input().split()))

d = dict()
t, c = 0, 0

for i in range(len(array)):
    c += array[i]
    t += (i + 1) * array[i] - c

    if array[i] in d:
        d[array[i]] += 1
    else:
        d[array[i]] = 1

    if (array[i] + 1) in d:
        t += d[array[i] + 1]
    if (array[i] - 1) in d:
        t -= d[array[i] - 1]

print(t)
