
N = int(input())


x_freq = {}
y_freq = {}

data = []
for i in range(4 * N + 1):
    arr = input()
    x, y = [int(x) for x in arr.split(' ')]
    data.append([x, y])

    if x not in x_freq:
        x_freq[x] = 1
    else:
        x_freq[x] += 1

    if y not in y_freq:
        y_freq[y] = 1
    else:
        y_freq[y] += 1

x_inteval = []
y_inteval = []

for num in x_freq:
    if x_freq[num] >= (N):
        x_inteval.append(num)

for num in y_freq:
    if y_freq[num] >= (N):
        y_inteval.append(num)

x_inteval = [min(x_inteval), max(x_inteval)]
y_inteval = [min(y_inteval), max(y_inteval)]
for p in data:
    if (p[0] not in x_inteval) and (p[1] not in y_inteval):
        print(p[0], p[1])
        quit()
    elif p[0] < x_inteval[0] or p[0] > x_inteval[1]:
        print(p[0], p[1])
        quit()
    elif p[1] < y_inteval[0] or p[1] > y_inteval[1]:
        print(p[0], p[1])
        quit()
