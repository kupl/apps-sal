import re
t = int(input())
for _ in range(t):
    n = int(input())
    names = set(input().split())
    m = int(input())
    dp = []
    a = []
    for i in range(m):
        a.append(input())
    for i in range(m):
        sender, msg = a[i].split(':')
        ls = set([_f for _f in re.split('\W+', msg) if _f])
        dp.append((names if sender == '?' else set([sender])) - ls)
        if i and len(dp[i - 1]) == 1:
            dp[i] -= dp[i - 1]
        # print(dp[i]);
    if any([len(p) == 0 for p in dp]):
        print("Impossible")
    else:
        res = []
        for i in reversed(list(range(m))):
            res.append(dp[i].pop())
            if i > 0:
                dp[i - 1].discard(res[-1])
        for i in range(m):
            sender, msg = a[i].split(':')
            sender = res[m - i - 1]
            print(sender + ':' + msg)
