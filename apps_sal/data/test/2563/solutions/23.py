q = int(input())
for t in range(q):
    s = input()
    ch = []
    nch = []
    for i in range(len(s)):
        if int(s[i]) % 2 == 0:
            ch.append(int(s[i]))
        else:
            nch.append(int(s[i]))
    ans = []
    i1 = 0
    i2 = 0
    while i1 < len(ch) and i2 < len(nch):
        if ch[i1] < nch[i2]:
            ans.append(ch[i1])
            i1 += 1
        else:
            ans.append(nch[i2])
            i2 += 1
    while i2 < len(nch):
        ans.append(nch[i2])
        i2 += 1
    while i1 < len(ch):
        ans.append(ch[i1])
        i1 += 1
    for i in range(len(ans)):
        print(ans[i], end='')
    print()
