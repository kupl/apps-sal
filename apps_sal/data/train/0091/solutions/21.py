t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    used = [0 for i in range(n + 2)]
    ans = []
    minimum = 1
    ans.append(a[0])
    used[a[0]] = 1
    if a[0] == 1:
        minimum = 2
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            ans.append(a[i])
            used[a[i]] = 1
            if a[i] == minimum:
                minimum += 1
        else:
            ans.append(minimum)
            used[minimum] = 1
            while used[minimum] == 1:
                minimum += 1
    maximum = 0
    flag = True
    for i in range(len(ans)):
        maximum = max(maximum, ans[i])
        if a[i] != maximum:
            flag = False
    if flag and a[-1] == n:
        print(' '.join(map(str, ans)))
    else:
        print(-1)
