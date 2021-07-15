n, m = map(int, input().split())
for i in range(n):
    s = input()
    s = list(s)
    for j in range(len(s)):
        if s[j] == '.':
            if (i + j) % 2 == 0:
                s[j] = 'B'
            else:
                s[j] = 'W'
    print(''.join(s))
