our_list_1 = list(map(str, input()))
our_list_3 = list(map(str, input()))
our_list_2 = list(set(our_list_3))
output = 0
for i in range(len(our_list_2)):
    if our_list_2[i] not in our_list_1:
        print(-1)
        break
    output += min(our_list_3.count(our_list_2[i]), our_list_1.count(our_list_2[i]))
    if i == len(our_list_2) - 1:
        print(output)
