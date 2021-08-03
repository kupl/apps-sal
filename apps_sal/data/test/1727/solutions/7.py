from fileinput import *

data = []
for line in input():
    if lineno() == 1:
        [n] = list(map(int, line.split()))
    else:
        data.append(list(map(int, line.split())))

if n <= 2:
    o = n

else:
    o = 2

    for i in range(1, n - 1):
        rminus = data[i][0] - data[i][1]
        rplus = data[i][0] + data[i][1]

        if rminus > data[i - 1][0]:
            o += 1
        elif rplus < data[i + 1][0]:
            o += 1
            data[i][0] = rplus

print(o)
