for _ in range(int(input())):
    s = input()
    n = len(s)
    s += '$'
    i = 0
    ans = set()
    while i < n:
        c = s[i]
        if c != s[i + 1]:
            ans.add(c)
            i += 1
        else:
            i += 2
    print(''.join(sorted(ans)))

