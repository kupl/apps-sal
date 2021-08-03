def mp():
    return map(int, input().split())


n = int(input())
a = list(mp())

ans = 1
for i in range(1, n):
    if a[i] != a[0]:
        ans = i
a = a[::-1]
for i in range(1, n):
    if a[i] != a[0]:
        ans = max(ans, i)
print(ans)
