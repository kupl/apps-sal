N = int(input())
lucas_list = []
for i in range(N + 1):
    if i == 0:
        lucas_list.append(2)
    elif i == 1:
        lucas_list.append(1)
    else:
        lucas_list.append(lucas_list[-1] + lucas_list[-2])
else:
    print(lucas_list[-1])
