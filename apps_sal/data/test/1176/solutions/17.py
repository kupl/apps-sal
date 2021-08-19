N = int(input())
A = list(map(int, input().split()))
minus_cnt = 0
abs_sum = 0
min_abs_val = 1000000000
for i in range(N):
    abs_val = abs(A[i])
    abs_sum = abs_sum + abs_val
    if abs_val < min_abs_val:
        min_abs_val = abs_val
    if A[i] < 0:
        minus_cnt = minus_cnt + 1
B_max_sum = 0
if minus_cnt % 2 == 0 or min_abs_val == 0:
    B_max_sum = abs_sum
else:
    B_max_sum = abs_sum - min_abs_val * 2
print(B_max_sum)
