def getFacts(n):
    facts = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            facts.append(i)
            if i != n // i:
                facts.append(n // i)
    return facts


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (n + 1)
    mod = 10 ** 9 + 7
    for i in arr:
        facts = getFacts(i)
        vals = {}
        for j in facts:
            if j <= n:
                vals[j] = dp[j - 1]
        for j in facts:
            if j <= n:
                dp[j] += vals[j]
                dp[j] %= mod
        dp[1] += 1
    total = sum(dp) % mod
    print(total)


main()
