n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = a[1]
for i in range(1, n - 1):
    if abs(a[0] / 2 - a[i]) > abs(a[0] / 2 - a[i + 1]):
        ans = a[i + 1]
    else:
        break
print(a[0], ans)
