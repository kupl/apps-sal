n = int(input())
x_list = list(map(int, input().split()))


def my_func(x):
    return int((x * 2 + 1) // 2)


x_list_mean = my_func(sum(x_list) / len(x_list))
count = 0
for i in x_list:
    count += (i - x_list_mean) ** 2
print(count)
