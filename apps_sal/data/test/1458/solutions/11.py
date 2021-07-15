n = int(input())
s = input()
if list(s) == sorted(s):
    print('NO')
else:
    i = 0
    while s[i] <= s[i + 1]:
        i += 1
    print('YES')
    print(i + 1, i + 2)
