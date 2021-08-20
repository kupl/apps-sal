t = int(input())
while t > 0:
    t -= 1
    a = list(map(int, input().split()))
    s = input()
    ans = ''
    tmp = 0
    n = a[0]
    k = a[1]
    for i in range(n):
        if k >= 0:
            if s[i] == '1':
                tmp += 1
                if i == n - 1:
                    for x in range(tmp):
                        ans += '1'
            else:
                if k >= tmp:
                    ans += '0'
                    if i == n - 1:
                        for x in range(tmp):
                            ans += '1'
                else:
                    for x in range(tmp - k):
                        ans += '1'
                    ans += '0'
                    for x in range(k):
                        ans += '1'
                k -= tmp
        else:
            ans += s[i]
    print(ans)
