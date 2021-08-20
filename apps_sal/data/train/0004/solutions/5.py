t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pos = [0 for i in range(n + 1)]
    for i in range(n):
        pos[a[i]] = i
    ans = [-1 for i in range(n)]
    ans[0] = 1
    (l, r) = (pos[1], pos[1])
    for i in range(2, n + 1):
        l = min(l, pos[i])
        r = max(r, pos[i])
        if r - l == i - 1:
            ans[i - 1] = 1
        else:
            ans[i - 1] = 0
    print(''.join(map(str, ans)))
