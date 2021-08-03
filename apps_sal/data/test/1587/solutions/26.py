n = int(input())
s = input()
res = 0
tem = s.find('WR')
if tem == -1:
    print(res)
else:
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and s[i] != 'W':
            i += 1
        while i < j and s[j] != 'R':
            j -= 1
        if s[i] == 'W' and s[j] == 'R':
            res += 1
            i += 1
            j -= 1
    print(res)
