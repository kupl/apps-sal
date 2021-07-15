for _ in range(int(input())):
    s = input()
    ch0 = 0
    ch1 = 0
    for i in s:
        if i == '1':
            ch1 += 1
        else:
            ch0 += 1
    ans = min(ch0, ch1)
    if ans % 2 == 0:
        print('NET')
    else:
        print('DA')
