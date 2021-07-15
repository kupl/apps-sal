#   TaskA

import sys

n, k = list(map(int, sys.stdin.readline().split()))

rent_points = list(map(int, sys.stdin.readline().split()))

my_list = [-1] * n

my_list[0] = 0
for i in range(1, len(my_list)):
    for j in range(0, i):
        if rent_points[i] - rent_points[j] <= k and my_list[j] != -1:
            my_list[i] = my_list[j] + 1
            break

print(my_list[n - 1])

