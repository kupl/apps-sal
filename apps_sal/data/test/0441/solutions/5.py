n, p, s = map(int, input().split())
q = input()
a = []
x = 0
for i in q:
    if (i == '*' and x):
        a.append(x)
        x = 0
    elif i == '.':
        x += 1
if (x):
    a.append(x)

ans = 0
lena = len(a)
for i in range(lena):
    if (p > s):
        ans += min(a[i] // 2 + a[i] % 2, p)
        p -= min(a[i] // 2 + a[i] % 2, p)
        ans += min(a[i] // 2, s)
        s -= min(a[i] // 2, s)
    else:
        ans += min(a[i] // 2 + a[i] % 2, s)
        s -= min(a[i] // 2 + a[i] % 2, s)
        ans += min(a[i] // 2, p)
        p -= min(a[i] // 2, p)        
print(ans)
