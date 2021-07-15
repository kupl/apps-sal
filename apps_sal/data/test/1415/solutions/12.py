x, y, x0, y0 = list(map(int, input().split()))
s = input()
s = s[:len(s) - 1]
visited = [[False for i in range(y + 1)] for j in range(x + 1)]
visited[x0][y0] = True
ans = '1 '
cnt = 1
for i in s:
    if i == 'U':
        if x0 != 1:
            x0 -= 1
            if not visited[x0][y0]:
                ans += '1 '
                cnt += 1
                visited[x0][y0] = True
            else:
                ans += '0 '
        else:
            ans += '0 '
    elif i == 'D':
        if x0 != x:
            x0 += 1
            if not visited[x0][y0]:
                ans += '1 '
                cnt += 1
                visited[x0][y0] = True
            else:
                ans += '0 '
        else:
            ans += '0 '
    elif i == 'L':
        if y0 != 1:
            y0 -= 1
            if not visited[x0][y0]:
                ans += '1 '
                cnt += 1
                visited[x0][y0] = True
            else:
                ans += '0 '
        else:
            ans += '0 '
    else:
        if y0 != y:
            y0 += 1
            if not visited[x0][y0]:
                ans += '1 '
                cnt += 1
                visited[x0][y0] = True
            else:
                ans += '0 '
        else:
            ans += '0 '
z = str(x * y - cnt)
print(ans + z)

