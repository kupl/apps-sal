import math


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
# len_nums = len(numbers)
# min_index = numbers.index(1) + 1
# if min_index % (k - 1) == 0 or min_index == 1:
#     before_time = min_index // (k - 1)
# else:
#     before_time = min_index // (k - 1) + 1

# if (len_nums - min_index) % (k - 1) == 0:
#     after_time = (len_nums - min_index) // (k - 1)
# else:
#     after_time = (len_nums - min_index) // (k - 1)
# print(before_time + after_time)
print(math.ceil((n - 1) / (k - 1)))
