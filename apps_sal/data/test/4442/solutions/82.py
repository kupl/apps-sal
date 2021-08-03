a, b = map(int, input().split())


def dic():
    a_str, b_str = str(a), str(b)
    a_moji = a_str * b
    b_moji = b_str * a
    dic = {a_moji: 1, b_moji: 2}
    dic = sorted(dic.items())

    return dic[0][0]


print(dic())
