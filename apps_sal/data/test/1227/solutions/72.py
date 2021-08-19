n = str(input())
k = int(input())
l = len(n)


def f(dig, under, num):
    if num > l - dig:
        return 0
    if num == 0:
        return 1
    if dig == l - 1:
        if under:
            return int(n[dig])
        else:
            return 9
    if under:
        if n[dig] == '0':
            res = f(dig + 1, True, num)
            #print(dig, under, num, res, 'aaa')
            return res
        else:
            res = f(dig + 1, False, num)
            if int(n[dig]) > 1:
                res += (int(n[dig]) - 1) * f(dig + 1, False, num - 1)
            res += f(dig + 1, True, num - 1)
            #print(dig, under, num, res, 'bbb')
            return res
    else:
        res = f(dig + 1, False, num)
        res += 9 * f(dig + 1, False, num - 1)
        #print(dig, under, num, res, 'ccc')
        return res


ans = f(0, True, k)
print(ans)
