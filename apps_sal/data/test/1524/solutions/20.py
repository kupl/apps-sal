s = input()
ans = [0] * len(s)
x = 0
y = 'R'
z = []
for i in s:
    if y == i:
        x += 1
    else:
        z.append([y, x])
        x = 1
        y = i
z.append([y, x])
ans = [0] * len(s)
i = 0
j = 0
while i < len(z):
    x = z[i][1]
    if z[i][0] == 'R':
        j += x - 1
        if x % 2 == 0:
            ans[j] += x // 2
        else:
            ans[j] += x // 2 + 1
        ans[j + 1] += x // 2
        j -= x - 1
        j += x
    if z[i][0] == 'L':
        if x % 2 == 0:
            ans[j] += x // 2
        else:
            ans[j] += x // 2 + 1
        ans[j - 1] += x // 2
        j += x
    i += 1
print(' '.join(map(str, ans)))
