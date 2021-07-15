n = int(input())
rg = []
for i in range(n):
    a, b = map(int, input().split())
    rg.append((a, b))
rg.sort()
last = rg[0][1]
ans = 1
for i in rg[1:]:
    if i[0] > last:
        last = i[1]
        ans += 1
    elif i[1] < last:
        last = i[1]
print(ans)
