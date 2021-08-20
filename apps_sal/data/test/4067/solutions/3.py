n = int(input())
a = list(map(int, list(input())))
cs = [0, 0, 0]
for i in a:
    cs[i] += 1
ops = 0
for i in cs:
    ops += max(0, i - n // 3)
if cs[0] < n // 3:
    for i in range(n):
        if a[i] != 0 and cs[a[i]] > n // 3:
            cs[a[i]] -= 1
            a[i] = 0
            cs[0] += 1
        if cs[0] == n // 3:
            break
if cs[2] < n // 3:
    for i in range(n - 1, -1, -1):
        if a[i] != 2 and cs[a[i]] > n // 3:
            cs[a[i]] -= 1
            a[i] = 2
            cs[2] += 1
        if cs[2] == n // 3:
            break
if cs[1] < n // 3:
    for i in range(n - 1, -1, -1):
        if a[i] == 0 and cs[0] > n // 3:
            cs[0] -= 1
            a[i] = 1
            cs[1] += 1
        if cs[1] == n // 3:
            break
    for i in range(n):
        if cs[1] == n // 3:
            break
        if a[i] == 2 and cs[2] > n // 3:
            cs[2] -= 1
            a[i] = 1
            cs[0] += 1
print(''.join(list(map(str, a))))
