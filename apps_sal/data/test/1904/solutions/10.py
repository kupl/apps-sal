import math

n = int(input())
s = input()
A = [int(x) for x in input().split(' ')]

def f():
    dp = [[0]*5 for _ in [-1]*n]
    for i in reversed(range(n)):
        for hard in reversed(range(4)):
            if i+1 == n:
                temp1 = A[i]
                if s[i] == 'hard'[hard]:
                    if hard + 1 == 4:
                        temp2 = math.inf
                    else:
                        temp2 = 0
                else:
                    temp2 = 0
            else:
                temp1 = A[i] + dp[i+1][hard]
                if s[i] == 'hard'[hard]:
                    if hard + 1 == 4:
                        temp2 = math.inf
                    else:
                        temp2 = dp[i+1][hard+1]
                else:
                    temp2 = dp[i+1][hard]
            dp[i][hard] = min(temp1, temp2)
    return dp[0][0]

print(f())
