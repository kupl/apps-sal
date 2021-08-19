N = int(input())
A = list(map(int, input().split()))
minus_cnt = 0
abs_sum = 0
min_abs_val = 1000000000
for i in range(N):
    val = A[i]
    abs_val = abs(val)
    abs_sum += abs_val
    if abs_val < min_abs_val:
        min_abs_val = abs_val
    if val < 0:
        minus_cnt += 1
B_max_sum = abs_sum
if minus_cnt % 2 != 0 and min_abs_val != 0:
    B_max_sum -= min_abs_val * 2
print(B_max_sum)
