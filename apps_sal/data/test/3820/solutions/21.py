t = 1
for test in range(1, t + 1):
    (n, m) = list(map(int, input().split()))
    s = input()
    t = input()
    if n - m > 1:
        print('NO')
        continue
    tmp = s.find('*')
    if tmp == -1:
        if s == t:
            print('YES')
        else:
            print('NO')
    elif s[:tmp] == t[:tmp] and s[tmp + 1:] == t[m - (n - tmp - 1):]:
        print('YES')
    else:
        print('NO')
