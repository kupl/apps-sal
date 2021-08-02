def main():
    from decimal import Decimal

    N, A, B = list(map(int, input().split()))
    *v, = list(map(Decimal, input().split()))

    v.sort(reverse=True)

    max_average = sum(v[:A]) / A

    tail = v[A - 1]
    contained = [0] * (N + 1)
    s = 0
    for i, x in enumerate(v, start=1):
        if x == tail:
            s += 1
        contained[i] = s

    def choose(n, a):
        if n - a < a:
            return choose(n, n - a)
        x, y = 1, 1
        for i in range(a):
            x = x * (n - i)
            y = y * (i + 1)
        return x // y

    count = 0
    for k in range(A, B + 1):
        if (k > A) and (v[k - 1] != max_average): break
        count += choose(contained[-1], contained[k])

    print(max_average)
    print(count)


def __starting_point():
    main()

# editorial
# K個選んだときの品物の価値の平均の最大値と
# K+1個個選んだときの品物の価値の平均の最大値の差を比較

# v[:A]は一つの値からなる->平均値を下げずに要素を追加できる可能性
# v[:A]は異なる値を含む->範囲外の値はより小さいので要素を追加できない


__starting_point()
