n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] >= b[i]:
        cnt += b[i]
    else:
        cnt += a[i]
        b[i] -= a[i]
        cnt += min(b[i], a[i + 1])
        a[i + 1] -= min(b[i], a[i + 1])
print(cnt)
