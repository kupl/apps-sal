from fileinput import *

for line in input():
    if lineno() == 1:
        [n] = list(map(int, line.split()))
    else:
        data = list(map(int, line.split()))

data.sort()
time = [0] * n

cumsum = 0
count = 0
for i in range(1, n):
    cumsum = cumsum + data[i - 1]

    if cumsum > data[i]:
        time[i] = data[i]
        data[i] = 0
    else:
        time[i] = cumsum

print(n - data.count(0))
