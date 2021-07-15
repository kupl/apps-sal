for _ in range(int(input())):
    s = input()

    ones = []
    cnt = 0
    for i in s:
        if i == '1':
            cnt += 1
        else:
            if cnt != 0:
                ones.append(cnt)
                cnt = 0
    if cnt != 0:
        ones.append(cnt)

    ones.sort(reverse=True)
    print(sum(ones[::2]))

