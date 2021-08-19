s = input()
ans = 'WA'
if s[0] == 'A':
    if s[2:-1].count('C') == 1:
        index = s[2:-1].find('C') + 2
        if s[1:index].islower() and s[index + 1:].islower():
            ans = 'AC'
print(ans)
