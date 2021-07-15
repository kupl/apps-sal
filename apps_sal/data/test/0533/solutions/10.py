a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

minicards = ((k1-1)*a1) + ((k2-1)*a2)
ans = [0,0]

ans[0] = max(n-minicards,0)

if k1>k2:
    ans[1] += min(n//k2,a2)
    n -= min(n//k2,a2) * k2

    ans[1] += min(n//k1,a1)
    n -= min(n//k1,a1) * k1
else:
    ans[1] += min(n//k1,a1)
    n -= min(n//k1,a1) * k1

    ans[1] += min(n//k2,a2)
    n -= min(n//k2,a2) * k2

print(*ans)

