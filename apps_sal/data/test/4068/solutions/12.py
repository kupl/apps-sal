
url = "https://atcoder.jp//contests/abc129/tasks/abc129_c"

def main():
    n, m = list(map(int, input().split()))
    isbreak = [False] * (n+1)
    for _ in range(m):
        isbreak[int(input())] = True

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(i+1, min(i+3, n+1)):
            if not isbreak[j]:
                dp[j] += dp[i]
                dp[j] %= 1000000007
    print((dp[-1]))




def __starting_point():
    main()

__starting_point()
