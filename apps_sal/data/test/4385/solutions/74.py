num_list = []
count_cant_go = 0

for i in range(5):
    num_list.append(int(input()))

num_list.append(int(input()))

if max(num_list) - min(num_list) <= num_list[-1]:
    print('Yay!')
else:
    print(':(')
