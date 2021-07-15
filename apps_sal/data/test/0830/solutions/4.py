import functools
import operator
info_data = list(map(int, input().split()))
data = list(map(int, input().split()))

aver = functools.reduce(operator.add, data) / info_data[0]

i = 0
result = []
while i < info_data[1]:
    max_v = data[0]
    min_v = data[0]
    max_j = 0
    min_j = 0
    for j in enumerate(data):
        if max_v < j[1]:
            max_v = j[1]
            max_j = j[0]
        if min_v > j[1]:
            min_v = j[1]
            min_j = j[0]

    if data[min_j] < aver:
        data[min_j] += 1
        data[max_j] -= 1
        result.append((max_j, min_j))
    else:
        break
    i += 1

max_v = data[0]
min_v = data[0]
max_j = 0
min_j = 0
for j in enumerate(data):
    if max_v < j[1]:
        max_v = j[1]
        max_j = j[0]
    if min_v > j[1]:
        min_v = j[1]
        min_j = j[0]


print("{} {}".format(max_v - min_v, i))
for i in result:
    print("{} {}".format(i[0]+1, i[1]+1))



