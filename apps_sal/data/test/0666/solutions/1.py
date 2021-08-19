def cel_sum(x):
    return x * (x + 1) // 2


n = int(input())
left = 0
right = 4 * n
while right - left > 1:
    mid = (right + left) // 2
    if cel_sum(mid) < n:
        left = mid
    else:
        right = mid
r = right
col = abs(n - cel_sum(r))
print(r - col)
