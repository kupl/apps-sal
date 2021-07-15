s = input()
x = 0
y = 'R'
rle = []
for c in s:
    if y == c:
        x += 1
    else:
        rle.append(x)
        x = 1
        y = c
rle.append(x)
ans = [0] * len(s)
i = 0
y = 'R'
for c in rle:
    if y == 'R':
        j = i + c - 1
        if c % 2 == 0:
            ans[j] += c // 2
        else:
            ans[j] += c // 2 + 1
        ans[j+1] += c // 2
        i += c
        y = 'L'
    else:
        if c % 2 == 0:
            ans[i] += c // 2
        else:
            ans[i] += c // 2 + 1
        ans[i-1] += c // 2
        i += c
        y = 'R'
print(' '.join(map(str,ans)))
