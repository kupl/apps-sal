import numpy
count = 0
N, D = map(int, input().split())

for i in range(N):
    x = input().split()
    y = numpy.sqrt(int(x[0]) ** 2 + int(x[1]) ** 2)
    if float(D) >= y:
        count += 1

print(count)
