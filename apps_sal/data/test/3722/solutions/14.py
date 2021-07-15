mod = 10**9 + 7

def main():
    n = int(input())
    caa = input()
    cab = input()
    cba = input()
    cbb = input()

    if n <= 3:
        print(1)
        return

    if cab == caa == 'A' or cab == cbb == 'B':
        print(1)
        return

    if cab == cba:
        dp = [0] * n
        dp[1] = 1
        for i in range(n-2):
            dp[i+2] = (dp[i] + dp[i+1]) % mod
        print(dp[n-1])
        return

    print(pow(2, n-3, mod))

main()
