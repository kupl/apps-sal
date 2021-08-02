def main():
    MOD = 10 ** 9 + 7

    s = input()
    n = len(s)

    acc_a = [0] * (n + 1)
    acc_c = [0] * (n + 1)
    acc_q = [0] * (n + 1)

    a = 0
    c = 0
    q = 0
    for i, char in enumerate(s, 1):
        if char == 'A':
            a += 1
        elif char == 'C':
            c += 1
        elif char == '?':
            q += 1
        acc_a[i] = a
        acc_c[i] = c
        acc_q[i] = q

    sq = [1]
    for _ in range(acc_q[n]):
        sq.append(sq[-1] * 3 % MOD)

    ans = 0
    qn = acc_q[n]
    for i, char in enumerate(s, 1):
        if char == 'B' or char == '?':
            is_q = int(char == '?')
            rq = acc_q[n] - acc_q[i]
            rc = acc_c[n] - acc_c[i]
            t = 0
            if qn - is_q >= 0:
                t += acc_a[i - 1] * rc * sq[acc_q[n] - is_q]
            if qn - 1 - is_q >= 0:
                t += acc_a[i - 1] * rq * sq[acc_q[n] - 1 - is_q]
                t += acc_q[i - 1] * rc * sq[acc_q[n] - 1 - is_q]
            if qn - 2 - is_q >= 0:
                t += acc_q[i - 1] * rq * sq[acc_q[n] - 2 - is_q]
            t %= MOD
            ans = (ans + t) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
