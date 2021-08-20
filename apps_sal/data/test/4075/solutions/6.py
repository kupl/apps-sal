(n, m) = map(int, input().split())
s = [list(map(int, input().split()))[1:] for i in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(1 << n):
    for j in range(m):
        c = 0
        for k in range(n):
            if i >> k & 1 and k + 1 in s[j]:
                c += 1
        if c % 2 != p[j]:
            break
    else:
        ans += 1
print(ans)
