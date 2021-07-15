import math
import sys
from sys import stdin, stdout

#sys.setrecursionlimit(300000)
# print(sys.getrecursionlimit())

# dp O(NlogN)
def getMinimunCost(a, sum, i, j, dp):

    if dp[i][j] != -1:
        return dp[i][j]

    if a[j] == -1:
        return 0

    remaining = sum[i] - j

    res = -2
    if i < len(dp)-1:
        min1 = getMinimunCost(a, sum, i+1, j+1, dp)
        if min1 != -2:
            res = min1 + a[j]

    if remaining > 0:
        min2 = getMinimunCost(a, sum, i, j+1, dp)
        if res == -2:
            res = min2
        elif min2 != -2:
            res = min(res, min2)

    dp[i][j] = res
    return dp[i][j]

def getMinimunCost2(a, sum, dp):

    if a[0] == -1:
        for j in range(0, len(dp[0])):
            dp[0][j] = 0
    else:
        for j in range(0, len(dp[0])):
            dp[0][j] = a[0]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if j <= sum[i]:
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + a[j])
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
                #break;

    #for i in range(len(dp)):
    #    print(dp[i])

    #print(a)

    return dp[-1][-1]


def __starting_point():
    try:
        n = int(stdin.readline())
        a = [int(i) for i in stdin.readline().split()]

        bcnt = int(math.log(n, 2))

        sum = []
        sum.append(0)

        x = int(n/2)
        for i in range(1, bcnt+1):
            sum.append(sum[i-1] + x)
            x = int(x/2)

        #dp = [[-1 for i in range(n)] for i in range(bcnt + 1)]
        dp = [[float("inf") for i in range(n)] for i in range(bcnt + 1)]

        #print(sum)
        #print(str(dp[0][0] + 1))

        #set 0
        flag = True
        for i in range(len(a)):
            if a[i] == -1:
                flag = False
                a[i] = 0
            if flag:
                a[i] = 0

        a.reverse()
        #res = getMinimunCost(a, sum, 0, 0, dp)
        res = getMinimunCost2(a, sum, dp)

        stdout.write(str(res))
    except BaseException as e:
        print(str(e))

__starting_point()
