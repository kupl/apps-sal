(n, k) = map(int, input().split())
l = list(map(int, input().split()))
cur = 0
for i in range(n):
    cur += l[i]
    k -= min(cur, 8)
    cur -= min(cur, 8)
    if k <= 0:
        print(i + 1)
        break
else:
    print(-1)
