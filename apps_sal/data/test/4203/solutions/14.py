s = input()
if s[0] != 'A':
    ans = 'WA'
else:
    c_cnt = s.count('C', 2, len(s) - 1)
    cnt = s.count('C')
    if c_cnt != 1 or c_cnt != cnt:
        ans = 'WA'
    else:
        s = s.replace('C', 'c')
        if s[1:].islower():
            ans = 'AC'
        else:
            ans = 'WA'
print(ans)
