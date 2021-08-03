A, B, X = map(int, input().split())


def nibutan(a, b, x):
    left_index = 1
    right_index = 10**9
    while left_index <= right_index:
        cc = (left_index + right_index) // 2
        if x - a * cc - b * (len(str(cc))) > 0:
            left_index = cc + 1
        elif x - a * cc - b * (len(str(cc))) == 0:
            return cc
        else:
            right_index = cc - 1
    return right_index


print(nibutan(A, B, X))
