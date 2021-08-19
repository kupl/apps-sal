from collections import defaultdict
INF = 100000000
t = 1
for test in range(t):
    n = int(input())
    a = list(list(map(int, input().split())))
    pre = [0 for i in range(n + 1)]
    for i in range(n):
        pre[i + 1] = pre[i] + a[i]
    Sum = defaultdict(list)
    for i in range(n):
        for j in range(i, n):
            tmp = pre[j + 1] - pre[i]
            Sum[tmp].append((i, j))
    maxVal = 0
    maxSum = -1
    for (key, val) in list(Sum.items()):
        val.sort()
        tmp = 1
        cur = val[0][1]
        for i in range(1, len(val)):
            if val[i][0] > cur:
                tmp += 1
                cur = val[i][1]
            elif val[i][1] <= cur:
                cur = val[i][1]
        if maxVal < tmp:
            maxVal = tmp
            maxSum = key
    print(maxVal)
    val = Sum[maxSum]
    val.sort()
    ans = []
    ans.append(val[0])
    cur = val[0][1]
    for i in range(1, len(val)):
        if val[i][0] > cur:
            ans.append(val[i])
            cur = val[i][1]
        elif val[i][1] <= cur:
            ans.pop()
            ans.append(val[i])
            cur = val[i][1]
    for i in ans:
        print(i[0] + 1, i[1] + 1)
