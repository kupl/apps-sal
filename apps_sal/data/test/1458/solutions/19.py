n = int(input())
s = input()
prev = ''
T = True
for i in range(1, len(s)):
    if ord(s[i]) < ord(s[i - 1]):
        print('YES')
        print(i, i + 1)
        T = False
        break
if T:
    print('NO')
