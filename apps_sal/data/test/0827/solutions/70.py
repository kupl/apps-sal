n = int(input())
t = input()

if n == 1:
    if t == '0':
        print((10 ** 10))
    elif t == '1':
        print((2 * (10 ** 10)))

elif n == 2:
    if t == '11' or t == '10':
        print((10 ** 10))
    elif t == '01':
        print((10 ** 10 - 1))
    else:
        print((0))

elif n == 3:
    if t not in ['110', '101', '011']:
        print((0))
        return

    if t == '110':
        print((10 ** 10))
    else:
        print((10 ** 10 - 1))

else:
    check_num_zero = list(set(t.split('1')))
    check_num_one = list(set(t.split('0')))
    for i in check_num_zero:
        if i not in ['', '0']:
            print((0))
            return
    for i in check_num_one:
        if i not in ['', '1', '11']:
            print((0))
            return

    ans = t.split('110')
    if set(ans) == {''}:
        ans = 10 ** 10 - len(ans) + 2
    elif ans[0] == '' or ans[-1] == '':
        ans = 10 ** 10 - len(ans) + 1
    else:
        ans = 10 ** 10 - len(ans)

    print(ans)
