n = int(input())
a = list(map(int, input().split()))
b = a[1:]
m = max(b)
ans = 0
mi = b.index(max(b))
while a[0] <= m:
    b[mi] -= 1
    ans += 1
    a[0] += 1
    m = max(b)
    mi = b.index(max(b))
print(ans)
