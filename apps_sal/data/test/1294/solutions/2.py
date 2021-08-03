for _ in range(int(input())):
    s = input()
    ans = set()
    cnt = 1
    c = s[0]
    for c1 in s[1:]:
        if c1 != c:
            if cnt % 2 == 1:
                ans.add(c)
            cnt = 1
            c = c1
        else:
            cnt += 1
    if cnt % 2 == 1:
        ans.add(c)
    print(''.join(sorted(ans)))
