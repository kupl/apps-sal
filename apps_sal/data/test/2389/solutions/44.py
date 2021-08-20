def main():
    (N, A, B, C) = map(int, input().split())
    s = [''] * (N + 1)
    for i in range(N):
        s[i] = str(input())
    dp = [''] * N
    (a, b, c) = ([0] * (N + 1), [0] * (N + 1), [0] * (N + 1))
    (a[0], b[0], c[0]) = (A, B, C)
    for i in range(N):
        if s[i] == 'AB':
            if a[i] + b[i] == 0:
                print('No')
                return
            elif a[i] == 1 and b[i] == 0:
                a[i + 1] = a[i] - 1
                b[i + 1] = b[i] + 1
                c[i + 1] = c[i]
                dp[i] = 'B'
            elif a[i] == 0 and b[i] == 1:
                a[i + 1] = a[i] + 1
                b[i + 1] = b[i] - 1
                c[i + 1] = c[i]
                dp[i] = 'A'
            elif a[i] == 0 and b[i] > 1:
                a[i + 1] = a[i] + 1
                b[i + 1] = b[i] - 1
                c[i + 1] = c[i]
                dp[i] = 'A'
            elif a[i] > 1 and b[i] == 0:
                a[i + 1] = a[i] - 1
                b[i + 1] = b[i] + 1
                c[i + 1] = c[i]
                dp[i] = 'B'
            elif a[i] == 1 and b[i] == 1:
                if s[i + 1] == '':
                    a[i + 1] = a[i] - 1
                    b[i + 1] = b[i] + 1
                    c[i + 1] = c[i]
                    dp[i] = 'B'
                elif s[i + 1] == 'AB':
                    a[i + 1] = a[i] + 1
                    b[i + 1] = b[i] - 1
                    c[i + 1] = c[i]
                    dp[i] = 'A'
                elif s[i + 1] == 'BC':
                    a[i + 1] = a[i] - 1
                    b[i + 1] = b[i] + 1
                    c[i + 1] = c[i]
                    dp[i] = 'B'
                elif s[i + 1] == 'AC':
                    a[i + 1] = a[i] + 1
                    b[i + 1] = b[i] - 1
                    c[i + 1] = c[i]
                    dp[i] = 'A'
            elif a[i] == 1 and b[i] > 1:
                a[i + 1] = a[i] + 1
                b[i + 1] = b[i] - 1
                c[i + 1] = c[i]
                dp[i] = 'A'
            elif a[i] > 1 and b[i] == 1:
                a[i + 1] = a[i] - 1
                b[i + 1] = b[i] + 1
                c[i + 1] = c[i]
                dp[i] = 'B'
            elif a[i] > 1 and b[i] > 1:
                if a[i] >= b[i]:
                    a[i + 1] = a[i] - 1
                    b[i + 1] = b[i] + 1
                    c[i + 1] = c[i]
                    dp[i] = 'B'
                elif a[i] < b[i]:
                    a[i + 1] = a[i] + 1
                    b[i + 1] = b[i] - 1
                    c[i + 1] = c[i]
                    dp[i] = 'A'
        elif s[i] == 'BC':
            if b[i] + c[i] == 0:
                print('No')
                return
            elif b[i] == 1 and c[i] == 0:
                b[i + 1] = b[i] - 1
                c[i + 1] = c[i] + 1
                a[i + 1] = a[i]
                dp[i] = 'C'
            elif b[i] == 0 and c[i] == 1:
                b[i + 1] = b[i] + 1
                c[i + 1] = c[i] - 1
                a[i + 1] = a[i]
                dp[i] = 'B'
            elif b[i] == 0 and c[i] > 1:
                b[i + 1] = b[i] + 1
                c[i + 1] = c[i] - 1
                a[i + 1] = a[i]
                dp[i] = 'B'
            elif b[i] > 1 and c[i] == 0:
                b[i + 1] = b[i] - 1
                c[i + 1] = c[i] + 1
                a[i + 1] = a[i]
                dp[i] = 'C'
            elif b[i] == 1 and c[i] == 1:
                if s[i + 1] == '':
                    b[i + 1] = b[i] - 1
                    c[i + 1] = c[i] + 1
                    a[i + 1] = a[i]
                    dp[i] = 'C'
                elif s[i + 1] == 'BC':
                    b[i + 1] = b[i] + 1
                    c[i + 1] = c[i] - 1
                    a[i + 1] = a[i]
                    dp[i] = 'B'
                elif s[i + 1] == 'AC':
                    b[i + 1] = b[i] - 1
                    c[i + 1] = c[i] + 1
                    a[i + 1] = a[i]
                    dp[i] = 'C'
                elif s[i + 1] == 'AB':
                    b[i + 1] = b[i] + 1
                    c[i + 1] = c[i] - 1
                    a[i + 1] = a[i]
                    dp[i] = 'B'
            elif b[i] == 1 and c[i] > 1:
                b[i + 1] = b[i] + 1
                c[i + 1] = c[i] - 1
                a[i + 1] = a[i]
                dp[i] = 'B'
            elif b[i] > 1 and c[i] == 1:
                b[i + 1] = b[i] - 1
                c[i + 1] = c[i] + 1
                a[i + 1] = a[i]
                dp[i] = 'C'
            elif b[i] > 1 and c[i] > 1:
                if b[i] >= c[i]:
                    b[i + 1] = b[i] - 1
                    c[i + 1] = c[i] + 1
                    a[i + 1] = a[i]
                    dp[i] = 'C'
                elif b[i] < c[i]:
                    b[i + 1] = b[i] + 1
                    c[i + 1] = c[i] - 1
                    a[i + 1] = a[i]
                    dp[i] = 'B'
        elif s[i] == 'AC':
            if c[i] + a[i] == 0:
                print('No')
                return
            elif c[i] == 1 and a[i] == 0:
                c[i + 1] = c[i] - 1
                a[i + 1] = a[i] + 1
                b[i + 1] = b[i]
                dp[i] = 'A'
            elif c[i] == 0 and a[i] == 1:
                c[i + 1] = c[i] + 1
                a[i + 1] = a[i] - 1
                b[i + 1] = b[i]
                dp[i] = 'C'
            elif c[i] == 0 and a[i] > 1:
                c[i + 1] = c[i] + 1
                a[i + 1] = a[i] - 1
                b[i + 1] = b[i]
                dp[i] = 'C'
            elif c[i] > 1 and a[i] == 0:
                c[i + 1] = c[i] - 1
                a[i + 1] = a[i] + 1
                b[i + 1] = b[i]
                dp[i] = 'A'
            elif c[i] == 1 and a[i] == 1:
                if s[i + 1] == '':
                    c[i + 1] = c[i] - 1
                    a[i + 1] = a[i] + 1
                    b[i + 1] = b[i]
                    dp[i] = 'A'
                elif s[i + 1] == 'AC':
                    c[i + 1] = c[i] + 1
                    a[i + 1] = a[i] - 1
                    b[i + 1] = b[i]
                    dp[i] = 'C'
                elif s[i + 1] == 'AB':
                    c[i + 1] = c[i] - 1
                    a[i + 1] = a[i] + 1
                    b[i + 1] = b[i]
                    dp[i] = 'A'
                elif s[i + 1] == 'BC':
                    c[i + 1] = c[i] + 1
                    a[i + 1] = a[i] - 1
                    b[i + 1] = b[i]
                    dp[i] = 'C'
            elif c[i] == 1 and a[i] > 1:
                c[i + 1] = c[i] + 1
                a[i + 1] = a[i] - 1
                b[i + 1] = b[i]
                dp[i] = 'C'
            elif c[i] > 1 and a[i] == 1:
                c[i + 1] = c[i] - 1
                a[i + 1] = a[i] + 1
                b[i + 1] = b[i]
                dp[i] = 'A'
            elif c[i] > 1 and a[i] > 1:
                if c[i] >= a[i]:
                    c[i + 1] = c[i] - 1
                    a[i + 1] = a[i] + 1
                    b[i + 1] = b[i]
                    dp[i] = 'A'
                elif c[i] < a[i]:
                    c[i + 1] = c[i] + 1
                    a[i + 1] = a[i] - 1
                    b[i + 1] = b[i]
                    dp[i] = 'C'
    print('Yes')
    for v in dp:
        print(v)


def __starting_point():
    main()


__starting_point()
