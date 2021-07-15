n = int(input())
l = [list(map(int,input().split())) for i in range(n-1)]
c,s,f = [list(i) for i in zip(*l)]
for _ in range(n-1):
    ans = 0
    for i in range(_,n-1):
        if ans < s[i]:
            ans = s[i]
        elif ans % f[i] == 0:
            pass
        else:
            ans += f[i] - (ans % f[i])
        ans += c[i]
    print(ans)
print(0)
