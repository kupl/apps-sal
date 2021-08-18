# -*- coding: utf-8 -*-
import numpy as np

# worst order: 101^6 => 10^8

c = []
c.append(list(map(int, input().split())))
c.append(list(map(int, input().split())))
c.append(list(map(int, input().split())))

arr_c = np.array(c)
a_max = np.amax(arr_c, axis=1)
b_max = np.amax(arr_c, axis=0)

a = []
b = []
for i in range(3):
    if len(list(range(0, a_max[i] + 1, 1))) == 0:
        a.append([0])
    else:
        a.append(list(range(0, a_max[i] + 1, 1)))

    if len(list(range(0, b_max[i] + 1, 1))) == 0:
        b.append([0])
    else:
        b.append(list(range(0, b_max[i] + 1, 1)))

ans = 'No'
cnt = 0
for a0 in a[0]:
    for b0 in b[0]:
        if c[0][0] != a0 + b0:
            continue
        for a1 in a[1]:
            if c[1][0] != a1 + b0:
                continue
            for b1 in b[1]:
                if c[0][1] != a0 + b1 or c[1][1] != a1 + b1:
                    continue
                for a2 in a[2]:
                    if c[2][0] != a2 + b0 or c[2][1] != a2 + b1:
                        continue
                    for b2 in b[2]:
                        if c[0][2] != a0 + b2 or c[1][2] != a1 + b2 or c[2][2] != a2 + b2:
                            continue

                        print("Yes")
                        return

print(ans)
