n = int(input())
s = input()
i = 2
ans = 1
while i < n:
    if s[i] == s[i - 1] and s[i] == '1':
        ans = 0
        break
    if s[i] == s[i - 1] and s[i] == s[i - 2]:
        ans = 0
        break
    i += 1
if n > 1 and s[0] == s[1]:
    ans = 0
if n > 1 and s[n - 1] == s[n - 2]:
    ans = 0
if n == 1 and s[0] == '0':
    ans = 0
if ans == 1:
    print('Yes')
else:
    print('No')
