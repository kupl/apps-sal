n, k = [int(i) for i in input().split()]
l = 0
r = 10 ** 13

while l < r:
    
    cur = (l + r + 1) // 2
    priz = cur * k
    if cur + priz <= n // 2:
        l = cur
    else:
        r = cur - 1

print(l, l * k, n - l - l * k)

