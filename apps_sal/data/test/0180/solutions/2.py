a = input()
k = int(input())

ml = 0
for i in a:
    if i == '?' or i == '*':
        ml -= 1
    else:
        ml += 1

if k < ml:
    print('Impossible')
    import sys
    return

dl = k - ml
t = ''
n = len(a)
for i in range(n):
    if i + 1 < n and a[i + 1] == '?':
        if dl <= 0:
            continue
        t += a[i]
        dl -= 1
        continue
    if i + 1 < n and a[i + 1] == '*':
        if dl <= 0:
            continue
        while dl > 0:
            t += a[i]
            dl -= 1
        continue
    if a[i] not in '?*':
        t += a[i]

if len(t) == k:
    print(t)
else:
    print('Impossible')
