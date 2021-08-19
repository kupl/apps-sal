import collections
import itertools
(n, m) = list(map(int, str.split(input())))
a = collections.deque(itertools.starmap(lambda i, s: (i, int(s)), enumerate(str.split(input()))))
while len(a) != 1:
    (i, c) = a.popleft()
    if c - m > 0:
        a.append((i, c - m))
(i, c) = a.popleft()
print(i + 1)
