(n, m) = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    flag = True
    for j in range(m):
        on = 0
        a = False
        for l in ks[j]:
            if a and i >> l - 1 & 1:
                on += 1
            a = True
        if on % 2 != p[j]:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
