s = input()
ans = False
n = len(s)
for i in range(n):
    for j in range(i + 1, n):
        if s[:i] + s[j:] == 'CODEFORCES':
            ans = True
            break
    if ans:
        break
if s[:10] == 'CODEFORCES':
    ans = True
if ans:
    print('YES')
else:
    print('NO')
