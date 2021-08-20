def ne(c):
    if c == 'L':
        return 'R'
    return 'L'


for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    if s[0] * n == s:
        ans += 1
        s = ne(s[0]) + s[0] * (n - 1)
    if s[0] == s[-1]:
        i = 0
        while s[i] == s[0]:
            i += 1
        s = s[i:] + s[:i]
    lst = '#'
    cnt = 0
    for i in range(n):
        if lst != s[i]:
            lst = s[i]
            ans += cnt // 3
            cnt = 1
        else:
            cnt += 1
    ans += cnt // 3
    print(ans)
