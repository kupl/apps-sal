import numpy as np
n = int(input())
x = list(map(int, input().split()))
median = np.median(x)
x_sorted = sorted(x)
index = len(x) // 2 - 1
for i in x:
    if i == median:
        print(i)
    elif i < median:
        print(x_sorted[index + 1])
    else:
        print(x_sorted[index])
