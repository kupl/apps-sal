s = input().split()
M = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (s[-1] == 'month'):
    x = int(s[0])
    ans = 0
    for i in range(12):
        if (M[i] >= x):
            ans += 1
    print(ans)
else:
    x = int(s[0])
    cur = 5
    ans = 0
    for i in range(366):
        if (cur == x):
            ans += 1
        cur += 1
        cur = (cur - 1) % 7 + 1
    print(ans)

