def f():
    n = int(input())
    M = [int(s) for s in input().split()]

    def goLeftFrom(s):
        sum = 0
        cur = M[s]
        for i in range(s - 1, -1, -1):
            cur = min(cur, M[i])
            sum += cur
        return sum

    def goRightFrom(s):
        sum = 0
        cur = M[s]
        for i in range(s + 1, n):
            cur = min(cur, M[i])
            sum += cur
        return sum
    ans = 0
    choose = -1
    for i in range(n):
        l = goLeftFrom(i)
        r = goRightFrom(i)
        if l + r + M[i] > ans:
            choose = i
            ans = l + r + M[i]
    rt = [0] * n
    s = choose
    rt[s] = M[s]
    cur = M[s]
    for i in range(s - 1, -1, -1):
        cur = min(cur, M[i])
        rt[i] = cur
    cur = M[s]
    for i in range(s + 1, n):
        cur = min(cur, M[i])
        rt[i] = cur
    print(' '.join(str(num) for num in rt))


f()
