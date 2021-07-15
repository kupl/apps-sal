def main():
    input()
    a = [int(c) for c in input().split()]
    s = list(input())

    sum_ = ans = 0
    for a_i, s_i in zip(a, s):
        if s_i == '1':
            ans = max(ans + a_i, sum_)
        sum_ += a_i


    print(ans)


def __starting_point():
    main()
__starting_point()
