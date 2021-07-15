for t in range(int(input())):
    s = input()
    c = input()
    ls = len(s)
    lc = len(c)
    for i in range(lc-1, -1, -1):
        if c[i] == '1':
            break
    ans = 0
    for j in range(ls-(lc-i), -1, -1):
        if s[j] == '1':
            break
        ans += 1
    print(ans)

