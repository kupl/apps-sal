N = int(input())
c_AA = input()
c_AB = input()
c_BA = input()
c_BB = input()
MOD = 10 ** 9 + 7

def fibonacchi(n, mod):
    dp = []
    for i in range(0, n):
        if i == 0 or i == 1:
            dp.append(1)
        else:
            dp.append((dp[i - 2] + dp[i - 1]) % mod)
    return dp[-1]

if N == 2 or N == 3:
    print((1))
else:
    if c_AB == 'B':
        if c_BB == 'B':
            print((1))
        else:
            if c_BA == 'A':
                print((pow(2, N - 3, MOD)))
            else:
                print((fibonacchi(N - 1, MOD)))
    else:
        if c_AA == 'A':
            print((1))
        else:
            if c_BA == 'A':
                print((fibonacchi(N - 1, MOD)))
            else:
                print((pow(2, N - 3, MOD)))

