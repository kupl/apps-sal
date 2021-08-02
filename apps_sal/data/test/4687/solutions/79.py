N, K = map(int, input().split())
l = [list(map(int, input().split()))for i in range(N)]
l.sort(key=lambda x: x[0])
ans = 0
for i in l:
    if K == 0:
        break
    K -= min(K, i[1])
    ans = i[0]
print(ans)
