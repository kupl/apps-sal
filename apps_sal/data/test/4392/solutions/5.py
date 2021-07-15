for _ in range(int(input())):
    a, b = map(int, input().split())
    s = list(map(int, input().split()))
    p = list(map(int, input().split()))
    i = 0
    check = 1
    ans = True
    while i != len(s) - check:
        if s[i] > s[i + 1]:
            s[i], s[i + 1] = s[i + 1], s[i]
            if i + 1 not in p:
                ans = False
            if i == 0:
                i -= 1
            else:
                i -= 2
        i += 1
    if ans:
        print('YES')
    else:
        print('NO')
