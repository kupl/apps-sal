t = int(input())
for i in range(t):
    n = int(input())
    (a, b, c) = map(int, input().split())
    s = input()
    count = 0
    ans = ['' for i in range(n)]
    for i in range(n):
        if s[i] == 'P' and c != 0:
            ans[i] = 'S'
            c -= 1
            count += 1
        if s[i] == 'S' and a != 0:
            a -= 1
            ans[i] = 'R'
            count += 1
        if s[i] == 'R' and b != 0:
            b -= 1
            count += 1
            ans[i] = 'P'
    for i in range(n):
        if ans[i] == '' and a != 0:
            ans[i] = 'R'
            a -= 1
        elif ans[i] == '' and b != 0:
            ans[i] = 'P'
            b -= 1
        elif ans[i] == '' and c != 0:
            ans[i] = 'S'
            c -= 1
    if count >= (n + 1) // 2:
        print('YES')
        print(*ans, sep='')
    else:
        print('NO')
