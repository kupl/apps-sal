t = int(input())
for i in range(t):
    s = input()
    ans = ''
    count = 0
    for j in range(1, 13):
        flag = False
        if 12 % j == 0:
            for p in range(12 // j):
                q = p
                while q < 12 and s[q] == 'X':
                    q += 12 // j
                if q >= 12:
                    flag = True
        if flag:
            ans += str(j) + 'x' + str(12 // j) + ' '
            count += 1
    print(count, ans[:-1])
