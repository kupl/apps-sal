input()
s = input()
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        print('YES')
        print(s[i] + s[i + 1])
        break
else:
    print('NO')
