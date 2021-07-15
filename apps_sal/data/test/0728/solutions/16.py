N = int(input())
x = [int(i) for i in input().split()]

import operator
iters = 0

while True:
    i, v = max(enumerate(x[1:]), key=operator.itemgetter(1))
    if x[0] > max(x[1:]):
        print(iters)
        break
    x[i + 1] -= 1
    x[0] += 1
    iters += 1

