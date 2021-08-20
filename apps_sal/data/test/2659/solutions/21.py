def sunuke_sum(arg):
    sum_digit = 0
    for char in arg:
        sum_digit += int(char)
    return sum_digit


input_num = int(input())
sunuke_dict = {}
min_sunuke_div = 10 ** 20
for d in reversed(range(1, 16)):
    for n in reversed(range(10, 1000)):
        i = n * 10 ** d + (10 ** d - 1)
        sunuke_div = i / sunuke_sum(str(i))
        sunuke_dict[i] = sunuke_div
for i in reversed(range(1, 110)):
    sunuke_div = i / sunuke_sum(str(i))
    sunuke_dict[i] = sunuke_div
sunuke_sorted = sorted(sunuke_dict.items())
sunuke_list = []
for (value, div_value) in reversed(sunuke_sorted):
    if min_sunuke_div >= div_value:
        sunuke_list.append(value)
        min_sunuke_div = div_value
sunuke_list.reverse()
for i in range(0, input_num):
    print(str(sunuke_list[i]))
