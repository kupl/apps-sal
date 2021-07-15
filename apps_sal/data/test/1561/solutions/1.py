n, m, k = list(map(int, input().split()))
a = []
ans = 0
for i in range(n):
    s = input()
    a.append(s)
    kk = 0
    for i in s:
        if i == '.':
            kk += 1
            if kk >= k:
                ans += 1
        else:
            kk = 0
for j in range(m):
    kk = 0
    for i in a:
        if i[j] == '.':
            kk += 1
            if kk >= k:
                ans += 1
        else:
            kk = 0
if k == 1:
    print(ans // 2)
else:
    print(ans)

