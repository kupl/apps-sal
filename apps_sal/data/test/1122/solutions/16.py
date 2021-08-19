# E
import numpy as np
n, m = list(map(int, input().split()))
lists = list(np.arange(1, n + 1))
list1 = lists[:m]
list2 = lists[m:]
num = m
for i in range(m // 2 + 1):
    if num == 0:
        break
    print(list2[i], list2[m + 1 - i - 1])
    num -= 1
    if num == 0:
        break
    print(list1[i], list1[m - i - 1])
    num -= 1
