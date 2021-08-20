s = input()
cntodda = 0
cntoddb = 0
cntevena = 0
cntevenb = 0
evencnt = 0
oddcnt = 0
for i in range(len(s)):
    oddcnt += 1
    if i % 2 == 0:
        if s[i] == 'a':
            evencnt += cntodda
            oddcnt += cntevena
        else:
            evencnt += cntoddb
            oddcnt += cntevenb
        if s[i] == 'a':
            cntevena += 1
        else:
            cntevenb += 1
    else:
        if s[i] == 'a':
            evencnt += cntevena
            oddcnt += cntodda
        else:
            evencnt += cntevenb
            oddcnt += cntoddb
        if s[i] == 'a':
            cntodda += 1
        else:
            cntoddb += 1
print(evencnt, oddcnt)
