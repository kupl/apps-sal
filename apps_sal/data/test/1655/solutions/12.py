n = int(input())
a = list(map(int, input().split()))
b = [1 for i in range(n)]
l = n
i = n - 1
while i >= 0:
    l = max(min(l, i - a[i]), 0)
    r = i - 1
    for i in range(r, l - 1, -1):
        b[i] = 0
        l = max(min(l, i - a[i]), 0)
    if r <= l - 1:
        i -= 1

ans = 0
for i in b:
    if i:
        ans += 1
print(ans)
