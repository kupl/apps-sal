n, m = map(int, input().split())
if m >= n:
    print(n)
    return

res = m + 1
n -= m
left, right = 0, int(1e19)

while right - left > 1:
    middle = (left + right) // 2
    if middle * (middle + 1) // 2 < n:
        left = middle
    else:
        right = middle

print(res + left)
