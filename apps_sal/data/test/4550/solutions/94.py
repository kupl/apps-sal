str_line = input().split(' ')
num_line = [int(n) for n in str_line]
num_line.sort()
if num_line[2] == num_line[1] + num_line[0]:
    print('Yes')
else:
    print('No')
