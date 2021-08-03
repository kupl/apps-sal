s = input()
ans = s + ''
l = len(s)
a = 'abcdefghijklmnopqrstuvwxyz'
i = 0
for j in range(26):
    while s[i] > a[j]:
        i += 1
        if i == l:
            print(-1)
            return
    ans = ans[:i] + a[j] + ans[i + 1:]
    i += 1
    if j != 25 and i == l:
        print(-1)
        return
print(ans)
