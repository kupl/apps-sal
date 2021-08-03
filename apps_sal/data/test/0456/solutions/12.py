n = int(input())
s = input()
ans = ''
cur = 0
while cur < n:
    if cur + 2 < n and s[cur:cur + 3] == 'ogo':
        ln = cur + 3
        while ln + 1 < n and s[ln:ln + 2] == 'go':
            ln += 2
        ans += '***'
        cur = ln
    else:
        ans += s[cur]
        cur += 1
print(ans)
