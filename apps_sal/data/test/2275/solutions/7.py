Q = int(input())
for _ in range(Q):
    n = int(input())
    s = input()
    while s != '' and s[0] == 'P':
        s = s[1:]

    ans = 0
    now = 0
    for i in s:
        if i == 'P':
            now += 1
        else:
            ans = max(ans, now)
            now = 0
    ans = max(ans, now)

    print(ans)

