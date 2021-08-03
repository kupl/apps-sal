import bisect
def input_split(f): return list(map(f, input().split()))


def main():
    n = int(input())
    a = sorted(list(input_split(int)))
    m = int(input())
    b = sorted(list(input_split(int)))
    res = -99999999999999
    res_str = ""
    res_a = -999999999999999

    def sum_p(p_list, d):
        if p_list[-1] < d:
            sum_a = len(p_list) * 2
        else:
            t = bisect.bisect_left(p_list, d)
            sum_a = t * 2 + (len(p_list) - t) * 3
        return sum_a

    for v in set(a + b + [99999999999999]):
        d = v
        sum_a = sum_p(a, d)
        sum_b = sum_p(b, d)
        import sys
        def dp(x): return sys.stderr.write(str(x) + "\n")
        dp("d:{}, a:{}, b:{}, res_a: {}".format(d, sum_a, sum_b, res_a))

        if res < sum_a - sum_b or (res == sum_a - sum_b and res_a < sum_a):
            res = sum_a - sum_b
            res_a = sum_a
            res_str = "{}:{}".format(sum_a, sum_b)
    print(res_str)


def __starting_point():
    main()


__starting_point()
