import math
a = int(input())
z = list(map(int, input().split()))
dp = [0 for i in range(max(z) + 1)]
dp[0] = 1


def fact(x):
    ans = []
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if x // i != i:
                ans.append(i)
                ans.append(x // i)
            else:
                ans.append(i)
    ans.append(x)
    return ans


for i in range(len(z)):
    t = fact(z[i])
    maxa = 0
    for i in range(len(t)):
        maxa = max(maxa, dp[t[i]])
    for i in range(len(t)):
        dp[t[i]] = maxa + 1
print(max(dp))
