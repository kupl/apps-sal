t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    if len(s) >= 11 and '8' in s[:-10]:
        print('YES')
    else:
        print('NO')
