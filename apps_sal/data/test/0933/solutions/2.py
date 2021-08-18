a = list(input())
x = ''
t = 0
y = 1
while t != len(a):
    if t == 0:
        x += a[t]
    else:
        if a[t] == a[t - 1]:
            y += 1
        else:
            x += a[t]
            y = 1
            t += 1
            continue
        if y > 2:
            t += 1
            continue
        else:
            x += a[t]
    t += 1
ans = ''
x = list(x)
i = 0

d = []
while i != len(x):
    if i == 0:
        d.append(x[i])
        i += 1
    else:
        if x[i] == x[i - 1]:
            d[-1] += x[i]
            i += 1
        else:
            d.append(x[i])
            i += 1
i = 0
while i != len(d):
    if i == 0:
        ans += d[i]
        i += 1
    else:
        if len(d[i - 1]) == 2:
            if len(d[i]) == 2:
                ans += d[i][0]
                d[i] = d[i][0]
            else:
                ans += d[i]
        else:
            ans += d[i]
        i += 1
print(ans)
