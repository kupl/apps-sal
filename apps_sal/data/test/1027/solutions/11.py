a = list(map(int, input().split()))
b = list()
for i in range(14):
    b.append(0)
ans = 0
ii = 0
for i in range(14):
    if a[i] > 0:
        for j in range(14):
            b[j] = a[j]
        tmp = b[i]
        cnt = b[i]//14
        tmp = b[i]%14
        b[i] = 0
        for j in range(14):
            b[j] = b[j]+cnt
        flag = (i+1)%14
        while tmp > 0:
            b[flag] = b[flag]+1
            tmp = tmp-1
            flag = (flag+1)%14
        res = 0
        for j in range(14):
            if b[j]%2 == 0:
                res = res+b[j]
        ans = max(ans, res)
print(ans)
