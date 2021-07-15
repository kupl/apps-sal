n = int(input())
a = list(map(int, input().split()))

g = [0 for i in range(43)]
ans = 0

for i in a:
    if i == 4:
        g[4] += 1
    elif i == 8:
        if g[4] > 0:
            g[4] -= 1
            g[8] += 1
        else:
            ans += 1
    elif i == 15:
        if g[8] > 0:
            g[8] -= 1
            g[15] += 1
        else:
            ans += 1
    elif i == 16:
        if g[15] > 0:
            g[15] -= 1
            g[16] += 1
        else:
            ans += 1
    elif i == 23:
        if g[16] > 0:
            g[16] -= 1
            g[23] += 1
        else:
            ans += 1
    elif i == 42:
        if g[23] > 0:
            g[23]-=1
        else:
            ans += 1
    else:
        ans += 1
ans += (g[4] + 2*g[8] + 3*g[15] + 4*g[16]+ 5*g[23])
print(ans)
