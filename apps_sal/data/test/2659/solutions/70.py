import numpy as np


def set_power(a, power_array):
    res = 1
    for i in range(len(power_array)):
        power_array[i] = res
        res *= a


def solve(ans, K, arr):
    p = 0
    for d in range(15):
        pow = arr[d]
        x = pow - 1
        for i in range(1, 10):
            if d > 2:
                y = i * pow + arr[d - 1] - 1
                if y <= (9 * (d - 1) + 1) * arr[d - 1]:
                    for j in range(0, 9):
                        if d > 9:
                            z = i * pow + j * arr[d - 1] + arr[d - 2] - 1
                            if z <= (9 * (d - 2) + j + 1) * arr[d - 2]:
                                for j2 in range(0, 9):
                                    ans[p] = z + j2 * arr[d - 2]
                                    p += 1
                        ans[p] = y + j * arr[d - 1]
                        p += 1
            ans[p] = i * pow + x
            p += 1
    return p


K = int(input())
ans = np.empty(10000, dtype=np.int64)
power_array = np.empty(16, dtype=np.int64)
set_power(10, power_array)
p = solve(ans, K, power_array)
print(*ans[:K].tolist(), sep='\n')
