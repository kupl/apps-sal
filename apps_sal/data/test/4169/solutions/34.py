a = list(map(int, input().split()))
b = []
ans = 0
cnt = a[1]
for i in range(a[0]):
    c = list(map(int, input().split()))
    b.append(c)
b = sorted(b)
for i in b:
    if cnt == 0:
        break
    ans += i[0] * min(cnt, i[1])
    cnt -= min(cnt, i[1])
print(ans)
