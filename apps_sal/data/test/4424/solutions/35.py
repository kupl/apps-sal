def ri(S):
    return [int(v) for v in S.split()]


def rii():
    return ri(input())


(K, X) = rii()
print('Yes' if K * 500 >= X else 'No')
