from itertools import count
X = int(input())
for t in count(1, 1):
    if (t - 1) * t >= 2 * (X - t):
        print(t)
        break
