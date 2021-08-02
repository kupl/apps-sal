import collections


input()
a = b = None
for _ in range(3):

    a, b = b, collections.Counter(str.split(input()))
    if a is not None:

        print(next(iter(a - b)))
