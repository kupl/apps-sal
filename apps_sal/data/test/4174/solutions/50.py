n, x = map(int, input().split())
l = list(map(int, input().split()))
list_d = [0]
ans = 0
for i in range(1, n + 1):
    list_d.append(list_d[i - 1] + l[i - 1])
for i in list_d:
    if i <= x:
        ans += 1
print(ans)
