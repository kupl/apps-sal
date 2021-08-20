(n, k) = map(int, input().split())
s = input()
ans = True
if s.find('G') > s.find('T'):
    s = s[::-1]
s = s[s.find('G')::k]
if s.find('T') != -1:
    s = s[:s.find('T') + 1]
    if '#' in s:
        ans = False
else:
    ans = False
if ans:
    print('YES')
else:
    print('NO')
