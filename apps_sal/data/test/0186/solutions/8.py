def check(x):
    return max(n - (x - 2) // 6 - (x - 4) // 6 - 2, 0) + \
           max(m - (x - 3) // 6 - 1, 0) <= x // 6


n, m = list(map(int, input().split()))
left, right = 0, 10 ** 10
while left + 1 < right:
    middle = (left + right) >> 1
    if check(middle):
        right = middle
    else:
        left = middle
print(right)

