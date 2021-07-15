t = int(input())
for j in range(t):
    n = int(input())
    s = input()
    f = True
    for i in range(n // 2):
        c = abs(ord(s[i]) - ord(s[n - i - 1]))
        if c != 0 and c != 2:
            f = False
            break
    if f:
        print('YES')
    else:
        print('NO')
