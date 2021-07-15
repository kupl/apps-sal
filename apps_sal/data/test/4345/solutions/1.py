# testing https://codeforces.com/contest/1144/submission/52125086

n = int(input())
a = [int(ai) for ai in input().split()] + [0]

inc, dec = -1, 10**6
marker = [0] * n

for i in range(n):
    if inc < a[i] and a[i] < dec:
        if a[i] < a[i + 1]:
            inc = a[i]
        else:
            dec = a[i]
            marker[i] = 1
    elif inc < a[i]:
        inc = a[i]
    elif dec > a[i]:
        dec = a[i]
        marker[i] = 1
    else:
        print('NO')
        break
else:
    print('YES')
    print(*marker)

