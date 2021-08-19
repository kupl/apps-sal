def f_takahashi_basics_in_education_and_learning(L, A, B, M, DIGIT_MAX=18):
    """numpyの行列演算だと L, A, B が 10**18 程度のときうまく動作しない"""

    def identity_matrix(n):
        """n×n単位行列"""
        return [[int(i == j) for i in range(n)] for j in range(n)]

    def multiply(a, b):
        """行列a, bの積"""
        row = len(a)
        col = len(b[0])
        t = len(b)
        ret = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                for k in range(t):
                    ret[i][j] += a[i][k] * b[k][j]
        for i in range(row):
            for j in range(col):
                ret[i][j] %= M
        return ret

    def power(a, k):
        """行列aのk乗"""
        n = len(a)
        ret = identity_matrix(n)
        while k:
            if k & 1:
                ret = multiply(ret, a)
            a = multiply(a, a)
            k >>= 1
        return ret
    num_pow_d = [0] * (DIGIT_MAX + 1)
    for d in range(DIGIT_MAX + 1):
        if 10 ** d - 1 < A:
            continue
        num_pow_d[d] = min((10 ** d - 1 - A) // B + 1, L)
    ans = 0
    array = [[0, A, 1]]
    for d in range(1, DIGIT_MAX + 1):
        c_d = num_pow_d[d] - num_pow_d[d - 1]
        matrix = [[10 ** d, 0, 0], [1, 1, 0], [0, B, 1]]
        array = multiply(array, power(matrix, c_d))
    return array[0][0]


(L, A, B, M) = [int(i) for i in input().split()]
print(f_takahashi_basics_in_education_and_learning(L, A, B, M))
