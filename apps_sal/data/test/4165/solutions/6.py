N = input()
num = list(map(int, input().split(' ')))
max_num = max(num)
num.remove(max_num)
num_sum = 0
for i in num:
    num_sum += i
if max_num < num_sum:
    print('Yes')
else:
    print('No')
