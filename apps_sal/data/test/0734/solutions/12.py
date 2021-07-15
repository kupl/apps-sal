n, m = map(int, input().split())
a = list(map(int, input().split()))
h = max(a)
a.sort()
a.reverse()
a.append(0)
ans = sum(a)
for i in range(n):
    if a[i + 1] >= a[i]:
        a[i + 1] = a[i] - 1
    ans -= max(a[i] - a[i + 1], 1)
print(ans)
