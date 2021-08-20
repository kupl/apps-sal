(x, y, a, b) = list(map(int, input().split()))
s = input()
m = [[0] * y for i in range(x)]
ans = '1 '
k = 1
m[a - 1][b - 1] = 1
for i in range(len(s)):
    if s[i] == 'D':
        a = min(a + 1, x)
        m[a - 1][b - 1] += 1
        if m[a - 1][b - 1] == 1:
            k += 1
            ans += '1 '
        else:
            ans += '0 '
    elif s[i] == 'U':
        a = max(a - 1, 1)
        m[a - 1][b - 1] += 1
        if m[a - 1][b - 1] == 1:
            k += 1
            ans += '1 '
        else:
            ans += '0 '
    elif s[i] == 'R':
        b = min(b + 1, y)
        m[a - 1][b - 1] += 1
        if m[a - 1][b - 1] == 1:
            k += 1
            ans += '1 '
        else:
            ans += '0 '
    else:
        b = max(b - 1, 1)
        m[a - 1][b - 1] += 1
        if m[a - 1][b - 1] == 1:
            k += 1
            ans += '1 '
        else:
            ans += '0 '
ans = ans[:-1]
k -= int(ans[-1])
ans = ans[:-1]
ans += str(x * y - k)
print(ans)
