import numpy as np
# in your code


def p(*args, **kargs):
    if DBG: print(*args, **kargs)


read = input
rn = lambda: list(map(int, read().split()))
debug = False


def sol(A):
    A = np.array(A, np.int64)
    A = np.sort(A)
    _A = np.sort(-A)

    pos = A[A > 0]
    neg = A[A < 0]
    zero = A[A == 0]

    def searchsorted(*args, **kargs):
        ret = np.searchsorted(*args, **kargs)

#         print(args, kargs)
#         print(ret)
        return ret

    # python 保证余数>0，即，整除，向无穷小round。
    # <= x，pairs that <= x
    def f(x):
        ret = 0
        if x >= 0:
            ret += len(zero) * len(A)
            ret += searchsorted(A, x // pos, side="right").sum()
            ret += searchsorted(_A, x // (-neg), side="right").sum()
        else:
            ret += searchsorted(A, x // pos, side="right").sum()
            ret += searchsorted(_A, x // (-neg), side="right").sum()

        ret -= np.count_nonzero(A * A <= x)
        assert ret % 2 == 0
        return ret // 2
        if debug: print(pos, neg, zero)
    return f


f = sol([-4, -2, 3, 3])
assert f(-12) == 2
assert f(-6) == 4  # or 3
# 二分搜索


def bs(A, index):
    A = np.array(A, np.int64)
    f = sol(A)
    max_ele = max(abs(A))

    right = max_ele * max_ele + 1
    left = - right
    while left + 1 < right:
        middle = (left + right) // 2
        m_index = f(middle)
        if debug: print(middle, m_index, left, right, sep="\t")
        if index <= m_index:
            right = middle
        else:
            left = middle
    return right


n, index = rn()
A = np.array(read().split(), np.int64)
print(bs(A, index))
