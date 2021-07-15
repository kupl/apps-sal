n = int(input())
l = 0
r = 10 ** 10
while l < r - 1:
    m = (l+r) // 2
    check = (m+1) * m // 2
    if check <= n + 1:
        l = m
    else:
        r = m
print(n - l + 1)
