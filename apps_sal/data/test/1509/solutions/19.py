n = int(input())
a = [0] + list(map(int, input().split()))

ans = 0

for i, j in zip(a[:-1], a[1:]):
    if i < j:
        ans += (j - i) * (n - j + 1)
    else:
        ans += j * (i - j)
print(ans)
