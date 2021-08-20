n = int(input())
for i in range(n):
    s = input()
    s1 = input()
    s = list(s)
    s.sort()
    f = False
    new_s = ''.join(s)
    for i in range(len(s1) - len(s) + 1):
        now = list(s1[i:len(new_s) + i])
        now.sort()
        now = ''.join(now)
        if now == new_s:
            f = True
    if f:
        print('YES')
    else:
        print('NO')
