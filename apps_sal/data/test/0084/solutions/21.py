nine = [0, 9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]


def get_answer(n):
    if (n < 5):
        return (n*(n-1))//2
    elif (2*n-1 in nine):
        return 1
    elif (n in nine):
        return (n-1)//2
    
    str_n = str(n)
    len_n = len(str_n)
    len_2n = len(str(2*n-1))
    
    if len_n == len_2n: # n < 50..0
        # pattern: A9..9, |9..9| = |n| - 1
        suf = "9" * (len_n - 1)
        k = int(suf)
        res = 0
        for c in range(10):
            if (int(str(c) + suf) <= 2*n-1):
                # print(str_n[0], c, '+', suf)
                if (int(str(c) + suf) <= n):
                    for i in range(c//2+1):
                        if i == c-i:
                            if i == 0:  # (0, 0): 01 -> 49
                                res += (k-1)//2
                            else:  # (1, 1): 00 -> 49
                                res += (k+1)//2
                        else:
                            if i == 0:  # (0, 1): 01 -> 99 
                                res += k
                            else:  # (1, 2): 00 -> 99
                                res += k+1
                else:
                    for i in range(c//2+1):
                        if i > int(str_n[0]) or c-i > int(str_n[0]):
                            continue
                        elif i < int(str_n[0]) and c-i < int(str_n[0]):
                            if i == c-i:
                                if i == 0:  # (0, 0): 01 -> 49
                                    res += (k-1)//2
                                else:  # (1, 1): 00 -> 49
                                    res += (k+1)//2
                            else:
                                if i == 0:  # (0, 1): 01 -> 99 
                                    res += k
                                else:  # (1, 2): 00 -> 99
                                    res += k+1
                        else:
                            # print(i, c-i, int(str(c) + suf), n)
                            if i != c - i:
                                # print(n-int(str_n[0])*(k+1)+1)
                                res += n-int(str_n[0])*(k+1)+1
                            else:
                                _n = int(str_n[1:])
                                # print(_n)
                                res += get_answer(_n) + (_n in nine)
                                # 99: (0, 0): 01 -> 49, (i, i): 00 -> 49 => +1
            else:
                break
        return res
    else: # n > 50..0
        # pattern: 9..9, |9..9| = |n|
        suf = int('9' * len_n)
        return n - (suf+1)//2 + 1

print(get_answer(int(input())))

