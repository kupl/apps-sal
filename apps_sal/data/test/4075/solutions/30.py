n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
p = list(map(int,input().split()))
ans = 0
for i in range(2**n):
    onoffs = [int(j) for j in list(bin(i)[2:].zfill(n))]
    Flag = True
    for lamp in range(m):
        k = a[lamp][0]
        info = [l - 1 for l in  a[lamp][1:]]
        tmp = 0
        for index in info:
            if onoffs[index]:
                tmp += 1
        if tmp % 2 != p[lamp]:
            Flag = False
            break
    if Flag:
        ans += 1
print(ans)
