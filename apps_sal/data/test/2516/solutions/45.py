N, P = map(int, input().split())
S = input()

if P == 2 or P == 5:
    def solve25(N, P, S):
        c = 0
        for i in range(N - 1, -1, -1):
            if int(S[i]) % P == 0:
                c += i + 1
        return c
    print(solve25(N, P, S))
else:
    def solve(N, P, S):
        rcounts = [0] * P
        rcounts[0] = 1
        ints = 0
        for i, s in enumerate(S[::-1]):
            ints += int(s) * pow(10, i, P)
            r = ints % P
            rcounts[r] += 1
        c = 0
        for v in rcounts:
            c += v * (v - 1) // 2
        return c
    print(solve(N, P, S))
