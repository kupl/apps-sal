n,m = list(map(int,input().split()))
s = []
for i in range(n):
    s.append(list(map(int,input().split())))
s.sort()
ans = 0
for i in s:
    if i[1]<m:
        ans += i[0]*i[1]
        m -= i[1]
    else:
        ans += i[0]*m
        break
print(ans)

