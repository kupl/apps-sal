n, m = map(int, input().split())
flag = 0
for i in range(n):
    if i % 2 == 0:
        print('
    else:
        if flag == 0:
            print('.' * (m - 1), '
            flag=(flag + 1) % 2
        else:
            print('
            flag=(flag + 1) % 2
