import sys
import math
(n, A, B) = list(map(int, sys.stdin.readline().strip().split(' ')))
arr = list(map(int, sys.stdin.readline().strip().split(' ')))
first_hole = arr[0]
sum_holes = sum(arr)
sorted_arr = sorted(arr[1:], reverse=True)
idx = 0
ans = 0
while first_hole * A / sum_holes < B:
    sum_holes -= sorted_arr[idx]
    idx += 1
    ans += 1
print(ans)
