t = int(input())
for _ in range(t):
    s = input()
    rcount = 0
    pcount = 0
    scount = 0
    for i in range(len(s)):
        if s[i] == 'R':
            rcount += 1
        if s[i] == 'S':
            scount += 1
        if s[i] == 'P':
            pcount += 1
    ans = []
    if rcount >= pcount and rcount >= scount:
        for i in range(len(s)):
            ans.append('P')
    elif scount >= pcount and scount >= rcount:
        for i in range(len(s)):
            ans.append('R')
    else:
        for i in range(len(s)):
            ans.append('S')
    print(''.join(ans))
