n = int(input())
a = list(map(int, input().split()))

mn = min(a)
pm = None
ans = n + 1
for i in range(n):
    if a[i] == mn:
        if pm is not None:
            ans = min(ans, i - pm)
        pm = i
print(ans)
