import itertools
n = int(input())
vals = list(map(int, input().split()))


def is_square(x):
    if x < 0:
        return False
    for i in itertools.count():
        if i ** 2 == x:
            return True
        if i ** 2 > x:
            return False


res = -10 ** 6 - 1
for x in vals:
    if x > res:
        if not is_square(x):
            res = x
print(res)
