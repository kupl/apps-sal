str_line = input().split(' ')
num_line = [int(n) for n in str_line]
num_line.sort()
num_list = [num_line[0]]
for i in range(1, len(num_line)):
    if num_line[i] != num_line[i - 1]:
        num_list.append(num_line[i])
print(len(num_list))
