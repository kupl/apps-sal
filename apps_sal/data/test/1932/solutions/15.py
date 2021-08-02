from sys import stdin, stdout

n = int(stdin.readline())
ans = 0

for i in range(n):
    s = stdin.readline().strip()

    if s[0] == 'T':
        ans += 4
    elif s[0] == 'C':
        ans += 6
    elif s[0] == 'O':
        ans += 8
    elif s[0] == 'D':
        ans += 12
    elif s[0] == 'I':
        ans += 20


stdout.write(str(ans))
