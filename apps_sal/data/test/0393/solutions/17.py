N = int(input())
chairs = input()
ones = 0
zeros = 1
flag = 1
for i in range(N):
    if chairs[i] == '0':
        zeros += 1
        ones = 0
        if zeros == 3:
            print('No')
            flag = 0
            break
    elif chairs[i] == '1':
        ones += 1
        zeros = 0
        if ones == 2:
            print('No')
            flag = 0
            break
    else:
        ones = 0
        zeros = 0
if zeros == 2:
    print('No')
elif flag == 1:
    print('Yes')
