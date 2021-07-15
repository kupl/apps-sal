import sys
n, k = list(map(int, input().split()))
s = input()
a = s.index('G')
b = s.index('T')
while a < b:
    b = b - k
    pos = b
    if pos >= 0 and (s[pos] == '.' or s[pos] == 'T'):
        pass
    else:
        break
while a > b:
    b = b + k
    pos = b
    if pos < n and (s[pos] == '.' or s[pos] == 'T'):
        pass
    else:
        break
if a != b:
    print('NO')
else:
    print('YES')
    

