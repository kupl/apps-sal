import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()

    dp = [[0] * 3 for _ in range(n + k)]
    for i1 in range(k):
        i2 = i1 + k
        while i2 - k < n:
            dp[i2][0] = max(dp[i2-k][1], dp[i2-k][2])
            dp[i2][0] += r if t[i2-k] == 's' else 0
            dp[i2][1] = max(dp[i2-k][0], dp[i2-k][2])
            dp[i2][1] += s if t[i2-k] == 'p' else 0
            dp[i2][2] = max(dp[i2-k][0], dp[i2-k][1])
            dp[i2][2] += p if t[i2-k] == 'r' else 0
            i2 += k
    r = 0
    for j1 in range(-k, 0, 1):
        r += max(dp[j1])
    print(r)

def __starting_point():
    main()
__starting_point()
