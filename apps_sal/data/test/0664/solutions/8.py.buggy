n = int(input())
a = list(map(int, input().split()))
k = -1
for i in range(n - 1):
    if a[i] > a[i + 1]:
        k = i + 1
        break
else:
    print(0)
    return
for i in range(k, n - 1):
    if a[i] > a[0] or a[i] > a[i + 1]:
        print(-1)
        return
if a[k] > a[0] or a[-1] > a[0]:
    print(-1)
else:
    print(n - k)
