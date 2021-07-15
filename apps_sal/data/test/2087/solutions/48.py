def sum_arith_prog(a, b, c):
    tmp_list = [a, b, c]
    for i in tmp_list:
        yield i * (i + 1) // 2


def main():
    a, b, c = list(map(int, input().split()))
    a_sum, b_sum, c_sum = sum_arith_prog(a, b, c)
    a_b_c_multi = a_sum * b_sum * c_sum
    ans = a_b_c_multi % 998244353
    print(ans)


def __starting_point():
    main()

__starting_point()
