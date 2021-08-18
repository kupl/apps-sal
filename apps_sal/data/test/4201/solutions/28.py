from itertools import product
h, w, k = map(int, input().split())
table = [list(input()) for i in range(h)]
count = 0
for rbit in product(range(2), repeat=h):
    for cbit in product(range(2), repeat=w):
        black = 0
        for row in range(h):
            for col in range(w):
                if table[row][col] == "
                black += 1
        if black == k:
            count += 1
print(count)
