s = list(input())
n = len(s)

c = 0
k = 0
while c == 0:
    if k == n:
        c = 1
    else:

        if k + 7 <= n - 1 and s[k] == 'd' and s[k + 1] == 'r' and s[k + 2] == 'e' and s[k + 3] == 'a' and s[k + 4] == 'm' and s[k + 5] == 'e' and s[k + 6] == 'r' and s[k + 7] == 'a':
            k += 5
        elif k + 6 <= n - 1 and s[k] == 'd' and s[k + 1] == 'r' and s[k + 2] == 'e' and s[k + 3] == 'a' and s[k + 4] == 'm' and s[k + 5] == 'e' and s[k + 6] == 'r':
            k += 7
        elif k + 4 <= n - 1 and s[k] == 'd' and s[k + 1] == 'r' and s[k + 2] == 'e' and s[k + 3] == 'a' and s[k + 4] == 'm':
            k += 5
        elif k + 6 <= n - 1 and s[k] == 'e' and s[k + 1] == 'r' and s[k + 2] == 'a' and s[k + 3] == 's' and s[k + 4] == 'e' and s[k + 5] == 'r' and s[k + 6] == 'a':
            k += 5
        elif k + 5 <= n - 1 and s[k] == 'e' and s[k + 1] == 'r' and s[k + 2] == 'a' and s[k + 3] == 's' and s[k + 4] == 'e' and s[k + 5] == 'r':
            k += 6
        elif k + 4 <= n - 1 and s[k] == 'e' and s[k + 1] == 'r' and s[k + 2] == 'a' and s[k + 3] == 's' and s[k + 4] == 'e':
            k += 5
        else:
            c = 1

if k == n:
    print('YES')
else:
    print('NO')
