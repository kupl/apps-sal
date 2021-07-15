import sys

left_right_max = 0
left_right_min = float('inf')
right_left_max = float('-inf')
right_left_min = float('inf')
r3_max = float('-inf')
r3_min = float('inf')

n = int(sys.stdin.readline().strip())

for idx in range(n):
    x, y = sys.stdin.readline().strip().split(' ')
    x = int(x)
    y = int(y)

    left_right_tmp = x + y
    if left_right_tmp > left_right_max:
        left_right_max = left_right_tmp
    if left_right_tmp < left_right_min:
        left_right_min = left_right_tmp

    right_left_tmp = x - y
    if right_left_tmp > right_left_max:
        right_left_max = right_left_tmp
    if right_left_tmp < right_left_min:
        right_left_min = right_left_tmp
        
    r3_tmp = y - x
    if r3_tmp > r3_max:
        r3_max = r3_tmp
    if r3_tmp < r3_min:
        r3_min = r3_tmp

print(max(left_right_max - left_right_min, right_left_max - right_left_min, r3_max - r3_min))
