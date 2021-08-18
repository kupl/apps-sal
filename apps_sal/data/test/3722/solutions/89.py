import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return list(map(int, input().split()))


sys.setrecursionlimit(10**9)

N = int(input())
AA = input()
AB = input()
BA = input()
BB = input()
mod = 10**9 + 7

if N <= 3:
    print((1))
elif AA == 'A' and AB == 'A':
    print((1))
elif BB == 'B' and AB == 'B':
    print((1))
elif (AA, AB, BA, BB) in [("A", "B", "A", "A"), ("B", "A", "B", "A"), ("B", "A", "B", "B"), ("B", "B", "A", "A")]:
    print((pow(2, N - 3, mod)))
else:
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = 1
    for i in range(1, N):
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % mod
        dp[i][1] = dp[i - 1][0] % mod
    print((dp[-1][1]))
