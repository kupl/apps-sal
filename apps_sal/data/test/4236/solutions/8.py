a = [False,] * 110
b = []
ans = 0
n, m = map(int, input().split())

for i in range(n):
    l, r = map(int, input().split())
    while l <= r:
        a[l] = True
        l += 1

for i in range(1, m + 1):
    if not a[i]:
        b.append(i)
        ans += 1

print(ans)
print(*b)
