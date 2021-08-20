def pad_zero(s, n):
    s = str(s)
    return ('0' * n + s)[-n:]


def main():
    N = int(input())
    F = [[int(f) for f in input().split(' ')] for i in range(N)]
    P = [[int(p) for p in input().split(' ')] for i in range(N)]
    total_profit = []
    for b in range(1, 2 ** 10):
        sale_bit = list(pad_zero(format(b, 'b'), 10))
        profit = 0
        for i in range(len(F)):
            f = F[i]
            p = P[i]
            profit += p[sum([fjk * int(s) for (fjk, s) in zip(f, sale_bit)])]
        total_profit.append(profit)
    print(max(total_profit))


main()
