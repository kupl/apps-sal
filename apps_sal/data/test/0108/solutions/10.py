s = list(input())
ch = 'a'
for i in range(len(s)):
    if s[i] <= ch:
        s[i] = ch
        if ch == 'z':
            ans = ''
            for i in range(len(s)):
                ans += s[i]
            print(ans)
            break
        ch = chr(ord(ch) + 1)
else:
    print(-1)
