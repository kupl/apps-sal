input_to_list = lambda: [int(i) for i in input().split()]
n, k = input_to_list()
values = input_to_list()
values.sort()
n -= 1
min_time = 0
while n >= 0:
    min_time += (values[n] - 1) * 2
    n -= k
print(min_time)

