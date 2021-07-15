from itertools import groupby
t = int(input())
for _ in range(t):
    correct = set()
    for k, it in groupby(input()):
        if len(tuple(it)) % 2:
            correct.add(k)
    print(*sorted(correct), sep='')
