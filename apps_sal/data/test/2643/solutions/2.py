def main():
    import numpy as np
    k, q = map(int, input().split())
    d = np.array(list(map(int, input().split())))
    for i in range(q):
        n, x, m = map(int, input().split())
        x %= m
        d_mod = d % m
        zero_d = k - np.count_nonzero(d_mod)
        d_mod_sum = np.sum(d_mod) + m * zero_d
        rep = (n - 1) // k
        rem = (n - 1) % k
        zero_rem = len(d_mod[:rem]) - np.count_nonzero(d_mod[:rem])
        rem_sum = np.sum(d_mod[:rem]) + m * zero_rem
        ans = n - 1 - (x + d_mod_sum * rep + rem_sum) // m
        print(ans)


def __starting_point():
    main()


__starting_point()
