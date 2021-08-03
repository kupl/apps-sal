q = int(input())
for t in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    ma = 1
    ans = '1'
    uk1 = a.index(1)
    uk2 = uk1
    while uk2 - uk1 + 1 != n:
        if uk2 == n - 1:
            uk1 -= 1
            ma = max(ma, a[uk1])
            if ma == uk2 - uk1 + 1:
                ans = ans + '1'
            else:
                ans = ans + '0'
        else:
            if uk1 == 0:
                uk2 += 1
                ma = max(ma, a[uk2])
                if ma == uk2 - uk1 + 1:
                    ans = ans + '1'
                else:
                    ans = ans + '0'
            else:
                if a[uk1 - 1] < a[uk2 + 1]:
                    uk1 -= 1
                    ma = max(ma, a[uk1])
                    if ma == uk2 - uk1 + 1:
                        ans = ans + '1'
                    else:
                        ans = ans + '0'
                else:
                    uk2 += 1
                    ma = max(ma, a[uk2])
                    if ma == uk2 - uk1 + 1:
                        ans = ans + '1'
                    else:
                        ans = ans + '0'
    print(ans)
