n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    x = min(a[i], b[i])
    b[i] -= x
    ans += x
    y = min(a[i + 1], b[i])
    ans += y
    a[i + 1] -= y
print(ans)
