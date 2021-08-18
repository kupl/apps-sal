'''
Created on 2019. 9. 21.

@author: kkhh88
'''

table = [1, 1, 2, 3, 5]
for i in range(5, 100000):
    table.append((table[i - 1] + table[i - 2]) % 1000000007)
s = input()

cnt = 1
tmp = 'x'
tcnt = 0
for i in range(len(s)):
    if s[i] == 'm' or s[i] == 'w':
        cnt = 0
        break

    if (s[i] == 'n' or s[i] == 'u') and tmp == s[i]:
        tcnt = tcnt + 1
    else:
        cnt = cnt * table[tcnt] % 1000000007
        tcnt = 1
        tmp = s[i]

print(cnt * table[tcnt] % 1000000007)
