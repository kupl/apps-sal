n = int(input())
for i in range(n):
    ans = ''
    k =''
    s = input().split(':')
    c = m=0
    for g in range(len(s)):
        if s[g] != '':
            c += 1
    if c == 8:
        for j in range(c):
            s[j] = (4-len(s[j]))*'0' + s[j]
            ans += s[j] +':'
    else:
        k = (8-c)*'0000:'
        for j in range(len(s)):
            if s[j] == '':
                ans += k
                k = ''
                m = 1
            else:
                s[j] = (4-len(s[j]))*'0' + s[j]
                ans += s[j] +':'
    ans += k
    ans = ans[:-1]
    print(ans)
