def f():
    n = int(input())
    A = [int(s) for s in input().split()]
    memo = [[None for j in range(n+1)] for i in range(n+1)]
    for i in range(n):
        memo[i][i] = [A[i],A[i],1]  # startEle, endEle, minlen
    for l in range(2,n+1):
        for left in range(0,n-l+1):
            right = left + l - 1  # [left, right]
            minLen = l
            shortestMid = right
            for mid in range(left+1,right+1):
                pre = memo[left][mid-1]
                post = memo[mid][right]
                combLen = pre[2] + post[2]
                if pre[1]==post[0]:
                    combLen -= 1
                if combLen < minLen:
                    minLen = combLen
                    shortestMid = mid
            pre = memo[left][shortestMid - 1]
            post = memo[shortestMid][right]
            startEle = pre[0]
            endEle = post[1]
            if pre[2] == 1:
                if pre[0] == post[0]:
                    startEle = pre[0] + 1
            if post[2] == 1:
                if pre[1] == post[0]:
                    endEle = post[0] + 1
            memo[left][right] = [startEle, endEle, minLen]
    # print(memo[0][n-1])
    print(memo[0][n-1][2])


f()
