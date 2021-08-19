for anynumber in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for (index, i) in enumerate(l):
        if i not in d.keys():
            d[i] = [index + 1, index]
        else:
            d[i] = [max(index - d[i][1], d[i][0]), index]
    for i in d.keys():
        d[i] = max(d[i][0], n - d[i][1])
    ans = [-1 for i in range(n)]
    for i in sorted(d.keys(), reverse=True):
        ans[d[i] - 1] = i
    for i in range(1, n):
        if ans[i] == -1:
            ans[i] = ans[i - 1]
        elif ans[i - 1] != -1:
            if ans[i - 1] < ans[i]:
                ans[i] = ans[i - 1]
    for i in range(n - 1):
        print(ans[i], end=' ')
    print(ans[n - 1])
