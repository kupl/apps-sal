import numpy
N = int(input())
a = numpy.array([int(i) for i in input().split()])
min = 10 ** 9 + 1
minus = 0
total = 0
for i in a:
    if i < 0:
        minus += 1
    if abs(i) < min:
        min = abs(i)
    total += abs(i)
if minus % 2 == 0:
    print(total)
else:
    print(total - min * 2)
