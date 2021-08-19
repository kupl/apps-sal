nine = [0, 9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]


def get_answer(n):
    if n < 5:
        return n * (n - 1) // 2
    elif 2 * n - 1 in nine:
        return 1
    elif n in nine:
        return (n - 1) // 2
    str_n = str(n)
    len_n = len(str_n)
    len_2n = len(str(2 * n - 1))
    if len_n == len_2n:
        suf = '9' * (len_n - 1)
        k = int(suf)
        res = 0
        for c in range(10):
            if int(str(c) + suf) <= 2 * n - 1:
                if int(str(c) + suf) <= n:
                    for i in range(c // 2 + 1):
                        if i == c - i:
                            if i == 0:
                                res += (k - 1) // 2
                            else:
                                res += (k + 1) // 2
                        elif i == 0:
                            res += k
                        else:
                            res += k + 1
                else:
                    for i in range(c // 2 + 1):
                        if i > int(str_n[0]) or c - i > int(str_n[0]):
                            continue
                        elif i < int(str_n[0]) and c - i < int(str_n[0]):
                            if i == c - i:
                                if i == 0:
                                    res += (k - 1) // 2
                                else:
                                    res += (k + 1) // 2
                            elif i == 0:
                                res += k
                            else:
                                res += k + 1
                        elif i != c - i:
                            res += n - int(str_n[0]) * (k + 1) + 1
                        else:
                            _n = int(str_n[1:])
                            res += get_answer(_n) + (_n in nine)
            else:
                break
        return res
    else:
        suf = int('9' * len_n)
        return n - (suf + 1) // 2 + 1


print(get_answer(int(input())))
