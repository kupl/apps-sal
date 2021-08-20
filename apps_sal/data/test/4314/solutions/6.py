import numpy as np
(h, w) = map(int, input().split())
a = [list(str(input())) for i in range(h)]
ans = np.array(a)
cnt = 0
for (i, grid) in enumerate(a):
    if '#' not in grid:
        ans = np.delete(ans, i - cnt, 0)
        cnt += 1
cnt = 0
for i in range(w):
    for (j, grid) in enumerate(a):
        if grid[i] == '#':
            break
    else:
        ans = np.delete(ans, i - cnt, 1)
        cnt += 1
for i in range(len(ans)):
    print(''.join(ans[i]))
