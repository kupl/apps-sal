n, p = map(int, input().split())
s = list(ord(i) - 97 for i in input())

for i in range(n - 1, -1, -1):
    for j in range(s[i] + 1, p):
        if (i < 1 or j != s[i - 1]) and (i < 2 or j != s[i - 2]):
            s[i] = j
            for i in range(i + 1, n):
                for j in range(p):
                    if (i < 1 or j != s[i - 1]) and (i < 2 or j != s[i - 2]):
                        s[i] = j
                        break
            print(''.join(chr(i + 97) for i in s))
            return
print('NO')
