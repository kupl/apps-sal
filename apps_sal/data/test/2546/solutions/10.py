def check(x, s, a, n):
    num = (n + 1) // 2
    cur = 0
    sum_ = 0
    for i in range(n - 1, -1, -1):
        (l, r) = a[i]
        if cur == num:
            break
        if l >= x:
            cur += 1
        elif l <= x and x <= r:
            cur += 1
            sum_ += x - l
    if cur == num and sum_ <= s:
        return True
    return False


q = int(input())
ans = []
for _ in range(q):
    (n, s) = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    a = sorted(a, key=lambda x: x[0])
    s = s - sum([l for (l, r) in a])
    (l, u) = (a[n // 2][0], 1000000000)
    while u - l > 1:
        md = (u + l) // 2
        if check(md, s, a, n) == True:
            l = md
        else:
            u = md
    ans.append(str(l))
print('\n'.join([x for x in ans]))
