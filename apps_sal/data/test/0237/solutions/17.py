from sys import stdin, stdout
(n, m, k) = map(int, stdin.readline().split())
left = k - 1
right = n - k
l = 1
r = m + 1
while r - l > 1:
    mid = (r + l) // 2
    cnt = mid
    if mid > left:
        cnt += (2 * mid - 1 - left) * left // 2
    else:
        cnt += mid * (mid - 1) // 2 + left - (mid - 1)
    if mid > right:
        cnt += (2 * mid - 1 - right) * right // 2
    else:
        cnt += mid * (mid - 1) // 2 + right - (mid - 1)
    if cnt <= m:
        l = mid
    else:
        r = mid
stdout.write(str(l))
