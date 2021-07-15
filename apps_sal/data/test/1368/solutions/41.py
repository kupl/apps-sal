def d_maximum_average_sets():
    from functools import reduce
    N, A, B = [int(i) for i in input().split()]
    V = sorted([int(i) for i in input().split()], reverse=True)

    def combination(n, r):
        numerator = reduce(lambda x, y: x * y, range(n, n - r, -1))
        denominator = reduce(lambda x, y: x * y, range(1, r + 1))
        return numerator // denominator

    if V[0] == V[A - 1]:  # V の上位 A 個がすべて同じ値 (v_max とおく)
        # V で値が v_max である x 個から A 個以上 B 個以下選ぶ
        x = V.count(V[0])
        count = sum([combination(x, i) for i in range(A, B + 1)])
    else:
        # 上位 A 個のうち最も値が小さな要素の値を v_min とおき、
        # v_min が上位 A 個のうち a 個あったとする。
        # V で値が v_min である x 個から a 個選ぶ。
        v_min = V[A-1]
        x, a = V.count(v_min), V[:A].count(v_min)
        count = combination(x, a)
    return '{}\n{}'.format(sum(V[:A]) / A, count)

print(d_maximum_average_sets())
