n = int(input())
s = input()
for i in range(1, n):
    if s[i - 1] == s[i] and s[i] != '?':
        print('No')
        return
for i in range(1, n):
    if s[i - 1] == '?' and s[i] == '?':
        print('Yes')
        return
for i in range(1, n - 1):
    if s[i - 1] == s[i + 1] and s[i] == '?':
        print('Yes')
        return
if s[0] == '?' or s[-1] == '?':
    print('Yes')
else:
    print('No')
