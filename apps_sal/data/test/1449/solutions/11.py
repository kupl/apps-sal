gans = []
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    u = []
    for i in range(1, n):
        if a[i] == a[i - 1]:
            continue
        u.append(a[i - 1])
    u.append(a[-1])
    if len(u) > 1 and k == 1:
        ans = -1
    elif k == 1:
        ans = 1
    elif len(u) == 1:
        ans = 1
    else:
        ans = (max(len(u) - 1 - 1, 0)) // (k - 1) + 1
    gans.append(ans)
print('\n'.join(map(str, gans)))

