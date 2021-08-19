(n, m) = map(int, input().split())
s = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    s.append(tmp[1:])
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    for j in range(m):
        count = 0
        check = True
        for k in s[j]:
            if i >> k - 1 & 1:
                count += 1
        if count % 2 != p[j]:
            check = False
            break
    if check:
        ans += 1
print(ans)
