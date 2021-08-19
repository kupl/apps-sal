def __starting_point():
    n, a, y = input().strip().split(' ')
    n, a, y = [int(n), int(a), int(y)]
    bin_str = str(input())
    p = 0
    flag = 0
    for x in range(0, len(bin_str)):
        if bin_str[x] == '0':
            flag = 1
        elif bin_str[x] == '1' and flag == 1:
            flag = 0
            p += 1
    if flag == 1 and bin_str[x - 1]:
        p += 1
    # print(p)#***
    if p == 0:
        print('0')
    else:
        ans = ((p - 1) * min(a, y)) + y
        print(ans)


__starting_point()
