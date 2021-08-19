t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    k = [0, 2]
    flag = 0
    for i in range(0, n // 2):
        if abs(ord(s[i]) - ord(s[n - i - 1])) not in k:
            flag = 1
    if flag == 0:
        print('YES')
    else:
        print('NO')
