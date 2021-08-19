def solve(n):
    return n * (n + 1) // 2


N = int(input())
left = 0
right = N + 1
while abs(right - left) > 1:
    mid = abs(right + left) // 2
    if solve(mid) <= N + 1:
        left = mid
    else:
        right = mid
print(N - left + 1)
