num_list = [int(s) for s in list(input())]
if sum(num_list) % 9 == 0:
    print('Yes')
else:
    print('No')
