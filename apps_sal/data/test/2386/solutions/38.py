n = int(input().strip())
input_line = list(map(int, input().strip().split(' ')))
for idx in range(n):
    input_line[idx] = input_line[idx] - (idx + 1)
input_line.sort()
min_num = input_line[0]
num_sum = 0
for idx in range(n):
    num_sum = num_sum + abs(input_line[idx] - min_num)
res = num_sum
for idx in range(1, n):
    point_dist = input_line[idx] - input_line[idx - 1]
    this_dist = num_sum + idx * point_dist - (n - idx) * point_dist
    num_sum = this_dist
    res = min(res, this_dist)
print(res)
