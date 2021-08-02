n = int(input())
# by count of opens
a = dict()
for pos in range(n):
    cur = input()
    ops = 0
    add = 0
    was = False
    for i in cur:
        if i == '(':
            ops += 1
            add += 1
        else:
            ops -= 1
            if ops < 0:
                was = True
            add = max(add - 1, 0)
    if was and add > 0:
        continue
    if ops in a:
        a[ops] += 1
    else:
        a[ops] = 1

ans = 0
for i in list(a.keys()):
    if (0 - i) in a:
        if i != 0:
            cur = min(a[i], a[0 - i])
            ans += cur
            a[i] -= cur
            a[0 - i] -= cur
        else:
            ans += a[0] // 2
print(ans)
