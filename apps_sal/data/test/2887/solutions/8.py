# cook your dish here
import sys

list_of_lists = []

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)


volume = list_of_lists[1]
temperature = list_of_lists[2]

after_volume = []
temp_deduction = 0
total_reduction = []

for i in range(list_of_lists[0][0]):
    for x in range(len(after_volume)):
        if (after_volume[x] - temperature[i] < 0):
            temp_deduction += after_volume[x]
            after_volume[x] = 0
        else:
            temp_deduction += temperature[i]
            after_volume[x] = after_volume[x] - temperature[i]
    if (volume[i] - temperature[i] < 0):
        temp_deduction += volume[i]
        after_volume[x] = 0
    else:
        # print(i)
        temp_deduction += temperature[i]
        after_volume.append(volume[i] - temperature[i])
        # print(after_volume)

    total_reduction.append(temp_deduction)
    temp_deduction = 0

    # print(after_volume)
print(*total_reduction)
