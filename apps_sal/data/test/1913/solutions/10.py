def x():
    res = '1'
    nulls = 0
    n = input()
    for i in input().split():
        if i[0] == '0':
            return [0]
        else:
            if not i[0] == '1':
                res = i
            elif not i.count('0') == len(i) - 1:
                res = i
            else:
                nulls += len(i) - 1

    return [res, '0' * nulls]


print(*x(), sep='')
