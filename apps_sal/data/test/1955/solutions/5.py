def ch(ind):
    vis = [0 for i in range(m)]
    k = 0
    for i in range(ind, -1, -1):
        if d[i] and not vis[d[i] - 1]:
            k += a[d[i] - 1]
            vis[d[i] - 1] = 1
        else:
            if k:
                k -= 1
    return 0 if k else -1


n, m = list(map(int, input().split()))
d = list(map(int, input().split()))
a = list(map(int, input().split()))
vis = [0 for i in range(m)]
mid = m
i = 0
while(i < n):
    if d[i] and not vis[d[i] - 1]:
        mid -= 1
        vis[d[i] - 1] = 1
    if mid:
        pass
    else:
        break
    i += 1
if i == n or not ch(n - 1):
    print('-1')
    return

l = i - 1
r = n - 1
while(l < r - 1):
    mx = (l + r) // 2
    if(ch(mx)):
        r = mx
    else:
        l = mx
print(l + 2)
