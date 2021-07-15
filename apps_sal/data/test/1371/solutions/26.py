from sys import stdin

def main():
    input = stdin.readline

    s = int(input())
    dp = [0] * (s + 1)
    dp[0] = 1
    for i in range(s):
        if dp[i] == 0:
            continue
        for x in range(3, s + 1):
            if i + x <= s:
                dp[i + x] += dp[i]
                dp[i + x] %= 1000000007
            else:
                break
    print(dp[s])
main()
