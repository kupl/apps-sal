n = int(input())
s = input().strip()
s1 = 0
s2 = 0
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i - 1] == 'S':
            s1 += 1
        else:
            s2 += 1
if s1 > s2:
    print('YES')
else:
    print('NO')
