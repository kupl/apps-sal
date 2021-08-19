(n, k) = list(map(int, input().split()))
s = sum(map(int, input().split()))
left = -1
right = 10 ** 100
while right - left > 1:
    mid = (left + right) // 2
    whole = s + k * mid
    if whole * 2 // (mid + n) < 2 * k - 1:
        left = mid
    else:
        right = mid
print(right)
