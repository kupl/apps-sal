A, B, K = list(map(int, input().split()))


def c_f(A, B):
    common_factor = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common_factor.append(i)
    return common_factor[-K]


print((c_f(A, B)))
