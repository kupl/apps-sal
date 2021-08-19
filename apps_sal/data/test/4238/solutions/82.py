temp = input()
temp = list(temp)
num_list = [int(s) for s in temp]
sum = 0
for i in range(len(num_list)):
    sum += num_list[i]
if sum % 9 == 0:
    print('Yes')
else:
    print('No')
