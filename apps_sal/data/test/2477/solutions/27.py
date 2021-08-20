(N, K) = map(int, input().split())
(*A,) = map(int, input().split())


def C(x):
    return sum([(A[i] - 0.5) // x for i in range(N)]) <= K


def binary_search2(func, n_min, n_max):
    (left, right) = (n_min, n_max)
    while right - left > 1:
        middle = (left + right) // 2
        y_middle = func(middle)
        if y_middle:
            right = middle
        else:
            left = middle
    return right


print(binary_search2(C, 0, max(A) + 1))
