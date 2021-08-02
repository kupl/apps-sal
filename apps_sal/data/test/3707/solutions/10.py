n, t, k, d = map(int, input().split())

first = (n // k)
if n % k != 0:
    first += 1

first = first * t

left = -1
right = int(1e9)
while right - left > 1:
    mid = (left + right) // 2

    one = (mid // t) * k
    two = (max(mid - d, 0) // t) * k
    if one + two >= n:
        right = mid
    else:
        left = mid


if right != first:
    print('YES')
else:
    print('NO')
