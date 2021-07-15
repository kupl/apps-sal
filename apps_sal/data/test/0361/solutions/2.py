s = input()

if s.startswith('CODEFORCES'):
    print('YES')
    return

for i in range(len(s)):
    for j in range(i):
        if s[:j] + s[i:] == 'CODEFORCES':
            print("YES")
            return

print("NO")

