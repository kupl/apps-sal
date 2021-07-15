s = int(input())

ans_list = [s]
curr_value = s
index = 1
while(True):
    if curr_value%2==0:
        curr_value = int(curr_value/2)
    else:
        curr_value = 3*curr_value + 1
    index += 1
    if curr_value in ans_list:
        break
    else:
        ans_list.append(curr_value)
print(index)
