# Proble D - Widespread

import math

# input
N, A, B = list(map(int, input().split()))
h_list = [0] * N
for i in range(N):
    h = int(input())
    h_list[i] = h

# initialization
left = 0
right = 10**10

# count
while right - left > 1:
    mid = (right + left) // 2

    # check
    count = 0
    for h in h_list:
        h = h - B * mid

        if h < 0:
            h = 0

        tmp_count = math.ceil(h / (A - B))
        count += tmp_count

    if count > mid:
        left = mid
    else:
        right = mid

# output
print(right)
