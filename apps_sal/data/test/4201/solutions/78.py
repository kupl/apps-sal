from itertools import product

h, w, k = map(int, input().split())
CC = [input() for _ in range(h)]

total = 0
for x in product((0, 1), repeat=w):
    for y in product((0, 1), repeat=h):
        count = 0
        for i in range(h):
            if y[i]:
                continue
            for j in range(w):
                if x[j]:
                    continue
                if CC[i][j] == '#':
                    count += 1
        if count == k:
            total += 1
print(total)
