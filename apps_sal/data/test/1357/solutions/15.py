3

n, m = tuple(map(int, input().split()))
a = [1] + list(map(int, input().split()))
ans = 0
for i, j in zip(a[:-1], a[1:]):
    ans += j - i if j >= i else n - i + j
print(ans)
