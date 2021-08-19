for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dpF = [0 for i in range(n)]
    dpB = [0 for i in range(n)]
    noRep = 1
    r = {}
    m = 0
    for i in range(n):
        if r.get(a[i]) == None:
            r[a[i]] = 1
            m = max(m, a[i])
            if m == i + 1:
                dpF[i] = 1
        else:
            break
    r = {}
    m = 0
    for i in range(n - 1, -1, -1):
        if r.get(a[i]) == None:
            r[a[i]] = 1
            m = max(m, a[i])
            if m == n - i:
                dpB[i] = 1
        else:
            break
    # print(dpF)
    # print(dpB)
    ans = 0
    ansList = []
    for i in range(n - 1):
        if dpF[i] == 1 and dpB[i + 1] == 1:
            ans += 1
            ansList.append([i + 1, n - i - 1])
    print(ans)
    for i in ansList:
        print(i[0], i[1])
