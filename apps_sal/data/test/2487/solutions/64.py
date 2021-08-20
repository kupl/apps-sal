n = int(input())
ans = n * (n + 1) * (n + 2) // 6
for i in range(n - 1):
    (l, r) = [int(i) for i in input().split()]
    if l > r:
        (l, r) = (r, l)
    ans -= l * (n - r + 1)
print(ans)
