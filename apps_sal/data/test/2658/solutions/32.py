n, k = [int(x) for x in input().split()]
a_list = [int(x) - 1 for x in input().split()]

ci = 0
temp_dict = {0: 0}
temp_list = [0]
for i in range(1, k + 1):
    temp = a_list[ci]
    if temp in temp_dict:
        ci = temp_list[(k - i) % (i - temp_dict[temp]) + temp_dict[temp]]
        break
    temp_dict[temp] = i
    temp_list.append(temp)
    ci = temp
print(ci + 1)
