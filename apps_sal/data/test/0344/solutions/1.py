s = input()
for i in range(len(s)):
    if s[i] in ['a', 'e', 'i', 'o', 'u', 'n']:
        continue
    elif i == len(s) - 1 or s[i + 1] not in ['a', 'e', 'i', 'o', 'u']:
        print('NO')
        break
else:
    print('YES')
