import numpy as np
N = int(input())
num_list = np.array(input().split(), dtype="int")

max_num = max(num_list)
max_bit_num = format(max_num, "b")
max_bit_num_length = len(max_bit_num)
ans = 0
radix = 1
for i in range(max_bit_num_length):
  new_num_list = (num_list >> i) & 1
  one_amount = np.count_nonzero(new_num_list == 1)
  zero_amount = len(num_list) - one_amount
  ans += (one_amount*zero_amount)*radix
  radix *= 2
print(ans%(10**9+7))
