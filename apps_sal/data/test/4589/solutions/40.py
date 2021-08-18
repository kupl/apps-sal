from collections import Counter
import math
import statistics
import itertools
a, b = map(int, input().split())
g = [list(map(lambda x: '{}'.format(x), list(input()))) for _ in range(a)]

for i in range(a):
    for k in range(b):
        count = 0
        if g[i][k] == ".":
            if k - 1 >= 0:
                if g[i][k - 1] == "
                count += 1
            if i - 1 >= 0:
                if g[i - 1][k] == "
                count += 1
            if i - 1 >= 0 and k - 1 >= 0:
                if g[i - 1][k - 1] == "
                count += 1
            if k + 1 <= b - 1:
                if g[i][k + 1] == "
                count += 1
            if i + 1 <= a - 1:
                if g[i + 1][k] == "
                count += 1
            if i + 1 <= a - 1 and k + 1 <= b - 1:
                if g[i + 1][k + 1] == "
                count += 1
            if i - 1 >= 0 and k + 1 <= b - 1:
                if g[i - 1][k + 1] == "
                count += 1
            if i + 1 <= a - 1 and k - 1 >= 0:
                if g[i + 1][k - 1] == "
                count += 1
            g[i][k] = str(count)


for i in g:
    print("".join(i))
