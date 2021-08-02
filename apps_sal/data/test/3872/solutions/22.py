memo_dict = {}


def equivalent(a, b):
    if a == b:
        return True

    if (a, b) in memo_dict:
        return memo_dict[(a, b)]

    strlen = len(a)

    if strlen % 2 != 0:
        return False

    a1, a2 = a[:strlen // 2], a[strlen // 2:]
    b1, b2 = b[:strlen // 2], b[strlen // 2:]

    res = (equivalent(a1, b1) and equivalent(a2, b2)) or (equivalent(a1, b2) and equivalent(a2, b1))

    memo_dict[(a, b)] = res
    memo_dict[(b, a)] = res

    return res


a = input()
b = input()

if equivalent(a, b):
    print('YES')
else:
    print('NO')
