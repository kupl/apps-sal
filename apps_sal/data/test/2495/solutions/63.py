def main():
    n = int(input())
    A = list(map(int, input().split()))

    ans = 0
    s = A[0]
    plus_flag = True
    if A[0] <= 0:
        ans += -A[0] + 1
        s = 1
    v1 = eval(s, ans, plus_flag, A)

    ans = 0
    s = A[0]
    plus_flag = False
    if A[0] >= 0:
        ans += A[0] + 1
        s = -1
    v2 = eval(s, ans, plus_flag, A)

    print((min(v1, v2)))


def eval(s, ans, plus_flag, A):
    for a in A[1:]:
        if plus_flag is True:
            plus_flag = False
            if s + a == 0:
                ans += 1
                s = -1
            elif s + a > 0:
                ans += s + a + 1
                s = -1
            else:
                s = s + a
        elif plus_flag is False:
            plus_flag = True
            if s + a == 0:
                ans += 1
                s = 1
            elif s + a < 0:
                ans += - (s + a) + 1
                s = 1
            else:
                s = s + a
    return ans


def __starting_point():
    main()


__starting_point()
