def f(n, a):
    x = list(sorted(set(a)))
    n_sub_half = n * (n + 1) // 2 // 2
    n_plus_minus = n * 2 + 1
    Li = 0
    Ri = len(x)
    while Ri > Li + 1:
        i = (Li + Ri) // 2
        xi = x[i]
        cnt_sum = [0] * n_plus_minus
        cumsum = 0
        cnt_sum[cumsum] = 1
        judge = 0
        s = 0
        for ak in a:
            if ak >= xi:
                cumsum += 1
                s += cnt_sum[cumsum] + 1
            else:
                cumsum -= 1
                s -= cnt_sum[cumsum + 1] - 1
            cnt_sum[cumsum] += 1
            judge += s
            if judge >= n_sub_half:
                Li = i
                break
        else:
            Ri = i
    print((x[Li]))


n = int(input())
a = list(map(int, input().split()))
f(n, a)
