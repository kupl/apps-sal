n = int(input())
s = input()


def bin_sear_pos(j, arr):
    initial = 0
    final = len(arr) - 1
    middle = (initial + final) // 2
    if arr[final] <= j:
        return final + 1
    elif arr[initial] > j:
        return initial
    while arr[middle] != j and (arr[middle] > j or arr[middle + 1] <= j):
        if arr[middle] < j:
            initial = middle
            middle = (initial + final) // 2
        else:
            final = middle
            middle = (initial + final) // 2

    return middle + 1


count_a = 0
count_b = 0
dic = {0: [], 1: []}
for i in range(n):
    if s[i] == "A":
        count_a += 1
        dic[0].append(i)
    else:
        count_b += 1
        dic[1].append(i)

count = 0
count += count_a * (count_a - 1) // 2
count += count_b * (count_b - 1) // 2
if count_a != 0 and count_b != 0:
    for i in range(len(dic[0]) - 1):
        # print("IN")
        b_pos = bin_sear_pos(dic[0][i], dic[1])

        # print(b_pos)
        if b_pos < len(dic[1]):
            count += len(dic[1]) - bin_sear_pos(max(dic[0][i + 1], dic[1][b_pos]), dic[1])
        # print(count)

    for i in range(len(dic[1]) - 1):
        a_pos = bin_sear_pos(dic[1][i], dic[0])
        if a_pos < len(dic[0]):
            count += len(dic[0]) - bin_sear_pos(max(dic[1][i + 1], dic[0][a_pos]), dic[0])


print(count)
