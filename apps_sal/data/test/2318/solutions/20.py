n = int(input())
for _ in range(n):
    s = input()
    t = input()
    i, j = 0, 0
    while i < len(s):
        c = s[i]
        x, y = 0, 0
        while i < len(s) and s[i] == c:
            i += 1
            x += 1
        while j < len(t) and t[j] == c:
            j += 1
            y += 1
        if x > y:
            print('NO')
            break
    else:
        print('YES' if j == len(t) else 'NO')

