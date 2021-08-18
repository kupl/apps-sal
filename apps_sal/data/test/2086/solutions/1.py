import sys
import math

f = sys.stdin

N = int(f.readline())
a = list(map(int, f.readline().split()))
start, end = list(map(int, f.readline().split()))

time_len = end - start
sum_p = 0
max_sum = -1
max_sum_end = 10000000
for i in range(N * 2):
    if i >= time_len:
        sum_p -= a[(i - time_len) % N]
    sum_p += a[i % N]
    ans = (2 * N + end - i - 1) % N
    if ans == 0:
        ans = N
    if i >= time_len - 1 and \
            (max_sum < sum_p or (max_sum == sum_p and max_sum_end > ans)):
        max_sum = sum_p
        max_sum_end = ans

print(max_sum_end)

'''
5
10 2 3 4 10
1 5

1 2 3 4 5
4 5 1 2 3
'''
