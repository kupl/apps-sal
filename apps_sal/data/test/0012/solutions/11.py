n = int(input())
s = input()
a = []
k = 1
for i in range(n - 1):
    if s[i] == 'G' and s[i + 1] == 'G':
        k += 1
    elif s[i] == 'G' and s[i + 1] == 'S':
        a.append([i, k])
        k = 1
if s[-1] == 'G':
    a.append([n - 1, k])
if len(a) == 0:
    print(0)
elif len(a) == 1:
    print(a[0][1])
elif len(a) == 2:
    ma = 0
    for i in a:
        ma = max(i[1], ma)
    ka = 0
    for i in range(len(a) - 1):
        if a[i + 1][0] - a[i + 1][1] + 1 - a[i][0] == 2:
            ka = max(a[i][1] + a[i + 1][1], ka)
    if ka > ma + 1:
        print(ka)
    else:
        print(ma + 1)
else:
    ma = 0
    for i in a:
        ma = max(i[1], ma)
    ka = 0
    for i in range(len(a) - 1):
        if a[i + 1][0] - a[i + 1][1] + 1 - a[i][0] == 2:
            ka = max(a[i][1] + a[i + 1][1], ka)
    print(max(ka, ma) + 1)
