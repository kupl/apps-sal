from collections import deque


def argmax(que, z):  # 二分求[i+1, a[i]]中a[x]最大的x
    l = 0
    r = len(que) - 1
    while (l <= r):
        mid = int((l + r) / 2)
        x = que[mid]['i']
        if (x <= z):
            r = mid - 1
        else:
            l = mid + 1
    return que[l]['i']


def solve(n, A):
    a = [0] * (n + 1)
    a[1:] = A
    dp = [0] * (n + 1)
    dp[n - 1] = 1
    que = deque()
    que.append({'i': n - 1, 'a': a[n - 1]})
    for i in range(n - 2, 0, -1):
        if (a[i] >= n):
            dp[i] = n - i
        else:
            x = argmax(que, a[i])
            dp[i] = x - i + dp[x] + n - a[i]
        while (len(que) > 0 and que[-1]['a'] < a[i]):
            que.pop()
        que.append({'i': i, 'a': a[i]})
    return sum(dp)


n = int(input())
a = list(map(int, input().split(' ')))
print(solve(n, a))
