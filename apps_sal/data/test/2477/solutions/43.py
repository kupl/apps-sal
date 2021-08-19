(n, k) = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = 10 ** 9
while r - l > 1:
    b = 0
    x = (l + r) // 2
    for i in range(n):
        b += (a[i] - 1) // x
    if k < b:
        l = x
    else:
        r = x
print(r)
