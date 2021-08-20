import numpy as np
N = int(input().rstrip())
h = [int(i) for i in input().rstrip().split()]
check = [0] * N
height = [0] * N
count = 0
while True:
    check = [1 if h[i] == height[i] else 0 for i in range(N)]
    if check.count(1) == N:
        break
    count += 1
    for i in range(N):
        if check[i] == 0:
            height[i] += 1
            if i < N - 1 and check[i + 1] == 1:
                break
print(count)
