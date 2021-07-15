s = input()
cnt = 0
if 'R' in s:
    if s[0] == s[1] or s[1] == s[2]:
        cnt = s.count('R')
    else:
        cnt += 1
print(cnt)
