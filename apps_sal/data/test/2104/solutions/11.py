import math


def mi():
    return list(map(int, input().split(' ')))


(l, r) = mi()
print('YES')
for i in range(l, r, 2):
    print(i, i + 1)
