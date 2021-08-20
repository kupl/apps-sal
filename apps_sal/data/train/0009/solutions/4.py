for nt in range(int(input())):
    s = input()
    n = len(s)
    if s[0] == '1':
        count = 1
    else:
        count = 0
    groups = []
    for i in range(1, n):
        if s[i] == '1':
            count += 1
        else:
            if count:
                groups.append(count)
            count = 0
    if count:
        groups.append(count)
    groups.sort(reverse=True)
    ans = 0
    for i in range(0, len(groups), 2):
        ans += groups[i]
    print(ans)
