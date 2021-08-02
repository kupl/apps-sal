s = input()
n = len(s)
t = s.lower()
if s[0] == 'A' and s.count('C') == 1 and s[1] != 'C' and s[n - 1] != 'C':
    cnt = 0
    for i in range(n):
        if s[i] != t[i]:
            cnt += 1
    if cnt == 2:
        print('AC')
        return
print('WA')
