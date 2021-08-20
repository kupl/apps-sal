from sys import stdin
cases = int(stdin.readline().strip())
for i in range(cases):
    n = int(stdin.readline().strip())
    s = stdin.readline().strip()
    if n > 2 or s[0] < s[1]:
        print('YES')
        print(2)
        print(s[0], s[1:])
    else:
        print('NO')
