import itertools
(h, w, k) = map(int, input().split())
fig = [list(input()) for _ in range(h)]
count = 0
for r_paint in itertools.product([0, 1], repeat=h):
    for c_paint in itertools.product([0, 1], repeat=w):
        kuro = 0
        for row in range(h):
            for col in range(w):
                if fig[row][col] == '#' and r_paint[row] == 0 and (c_paint[col] == 0):
                    kuro += 1
        if kuro == k:
            count += 1
print(count)
