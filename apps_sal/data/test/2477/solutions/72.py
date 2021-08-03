n, k = map(int, input().split())
a = list(map(int, input().split()))

low = 0
high = max(a)

while low + 1 < high:
    mid = (low + high) // 2
    m = 0
    for x in a:
        m += (x - 1) // mid

    if m <= k:
        high = mid
    else:
        low = mid

print(high)
