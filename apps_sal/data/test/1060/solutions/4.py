N = int(input())
List = [int(x) for x in input().split()]
MAX = 1000001
dp = [0] * MAX
for i in List:
    dp[i] += 1
for i in range(N):
    if dp[List[i]]:
        for j in range(List[i] * 2, MAX, List[i]):
            if dp[j]:
                dp[j] = max(dp[j], dp[List[i]] + 1)
print(max(dp))
