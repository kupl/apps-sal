P = 998244353
n = int(input().strip())
sub_sum = 0
curr_num = 1
for idx in range(n - 1):
    curr_num = curr_num * (n - idx) % P
    sub_sum = (sub_sum + curr_num) % P
add_num = curr_num * n % P
final = (add_num - sub_sum) % P
print(final)
