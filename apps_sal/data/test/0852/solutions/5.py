def inp(): return map(int, input().split())


t = int(input())
for _ in range(t):
    n, k, l = inp()
    d = list(inp())
    remain = [i for i in range((-1) * (k - 1), 0)] + [i for i in range(k + 1)]
    f = True
    for i in range(n):
        f = False
        new_remain = []
        for j in range(len(remain)):
            temp = (remain[j] + 1)
            if temp > k:
                temp = - k + 1
            if abs(temp) + d[i] <= l:
                f = True
                new_remain.append(temp)
        if not f:
            print("No")
            break
        remain = []
        flag = False if k + d[i] > l else True
        for j in range(1 - k, k + 1):
            if j in new_remain:
                flag = True
            if abs(j) + d[i] <= l and flag:
                remain.append(j)
            if abs(j) + d[i] > l:
                flag = False

    if f:
        print("Yes")
