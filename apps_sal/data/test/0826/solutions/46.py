n = int(input())
l = 0
r = 10**18
while r - l > 1:
    mid = (r + l) // 2
    sum = mid * (mid + 1)
    if sum <= 2 * (n + 1):
        l = mid
    else:
        r = mid

print(n - l + 1)
