def abc173_e():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 10**9 + 7

    A.sort(reverse=True)
    B = sorted(A, key=lambda x: abs(x), reverse=True)
    C = []

    if k == n:
        C = A
    elif k % 2 == 1 and A[0] < 0:
        C = A[:k]
    else:
        plus = []
        minus = []
        for b in B[:k]:
            if b >= 0:
                plus.append(b)
            else:
                minus.append(b)

        if len(minus) % 2 == 1:
            rem1, add1, rem2, add2 = None, None, None, None

            rem1 = minus[-1]
            add1 = max(B[k:])
            valid1 = (add1 >= 0)

            valid2 = False
            if plus:
                rem2 = plus[-1]
                add2 = min(B[k:])
                valid2 = (add2 < 0)

            if valid1 and valid2:
                if add1 * rem2 > rem1 * add2:
                    minus[-1] = add1
                else:
                    plus[-1] = add2
            elif valid1:
                minus[-1] = add1
            elif valid2:
                plus[-1] = add2

        C = plus + minus

    ans = 1
    for c in C:
        ans *= c
        if ans < 0:
            ans += mod
        ans %= mod
    print(ans)


def __starting_point():
    abc173_e()


__starting_point()
