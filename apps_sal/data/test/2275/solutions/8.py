def nex(s):
    l = len(s)
    t = s.copy()
    for i in range(l):
        if(i == 0):
            t[0] = s[0]
        else:
            if(s[i - 1] == 'A'):
                t[i] = 'A'
    return t


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    c = 0
    while(nex(s) != s):
        s = nex(s)
        c += 1
    print(c)
