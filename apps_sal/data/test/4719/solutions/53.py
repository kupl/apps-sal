import copy
n = int(input())
s = list(input())

if n == 1:
    s.sort()
    print(*s, sep='')
else:
    for _ in range(n-1):
        tmp = ''
        si = list(input())
        if len(si) >= len(s):
            for i in range(len(si)):
                if si[i] in s:
                    tmp += si[i]
                    s[s.index(si[i])], si[i] = '', ''
        else:
            for i in range(len(s)):
                if s[i] in si:
                    tmp += s[i]
                    si[si.index(s[i])], s[i] = '', ''
        s = list(copy.deepcopy(tmp))
    s.sort()
    print(*s, sep='')
