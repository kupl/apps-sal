t = int(input())
for i in range(t):
    (n, m) = map(int, input().split())
    a = set(map(int, input().split()))
    ans = [100000 for i in range(n)]
    l = -1
    for i in range(n):
        if i + 1 in a:
            l = 0
        if l != -1:
            l += 1
        if l != -1:
            ans[i] = min(ans[i], l)
    l = -1
    for i in range(n - 1, -1, -1):
        if i + 1 in a:
            l = 0
        if l != -1:
            l += 1
        if l != -1:
            ans[i] = min(ans[i], l)
    print(max(ans))
