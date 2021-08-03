a, b = map(int, input().split())
flag = 0

for i in range(1, 4):

    if (a * b * i) % 2 != 0:
        flag = 1
        break

    else:
        continue


if flag == 1:
    print('Yes')

else:
    print('No')
