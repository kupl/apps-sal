t = int(input())
for i in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    pr = [0] * n
    ans = [0] * n
    ans[0] = q[0]
    sh = 0
    s = set([q[0]])
    for i in range(1, n):
        if q[i] == q[i - 1]:
            pr[i] = pr[i - 1]
            sh += 1
        else:
            pr[i] = i
            ans[i] = q[i]
            s.add(q[i])
    steak = []
    for i in range(n, 0, -1):
        if i not in s:
            steak.append(i)
    tr = True
    for i in range(n):
        if ans[i] == 0:
            x = steak.pop()
            if x < q[pr[i]]:
                ans[i] = x
            else:
                tr = False
                break
    if tr:
        print(*ans)
    else:
        print(-1)
