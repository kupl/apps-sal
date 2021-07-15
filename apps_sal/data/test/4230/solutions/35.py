import numpy as np

x, y = list(map(int, input().split()))
p = input().split()
pn = [int(tmp) for tmp in p]

if y == 0:
    ans = x
elif not np.where(np.array(pn) == x)[0].size:
    ans = x
else:
    for i in range(1, 100):
        x1 = x + i
        x2 = x - i
        if not np.where(np.array(pn) == x2)[0].size:
            ans = x2
            break
        elif not np.where(np.array(pn) == x1)[0].size:
            ans = x1
            break
        else:
            continue

print(ans)

