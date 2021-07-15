t = 'CODEFORCES'

s = input()

for i in range(len(s)):
    for j in range(i, len(s) + 1):
        if ''.join((s[:i], s[j:])) == t:
            print('YES')
            return
print('NO')

