N = int(input())
flag = 0
for i in range(1, 10):
    for j in range(1, 10):
        if N == i * j:
            print('Yes')
            flag = 1
            break
    if flag == 1:
        break
if flag == 0:
    print('No')
