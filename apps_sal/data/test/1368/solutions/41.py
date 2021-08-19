def d_maximum_average_sets():
    from functools import reduce
    (N, A, B) = [int(i) for i in input().split()]
    V = sorted([int(i) for i in input().split()], reverse=True)

    def combination(n, r):
        numerator = reduce(lambda x, y: x * y, range(n, n - r, -1))
        denominator = reduce(lambda x, y: x * y, range(1, r + 1))
        return numerator // denominator
    if V[0] == V[A - 1]:
        x = V.count(V[0])
        count = sum([combination(x, i) for i in range(A, B + 1)])
    else:
        v_min = V[A - 1]
        (x, a) = (V.count(v_min), V[:A].count(v_min))
        count = combination(x, a)
    return '{}\n{}'.format(sum(V[:A]) / A, count)


print(d_maximum_average_sets())
