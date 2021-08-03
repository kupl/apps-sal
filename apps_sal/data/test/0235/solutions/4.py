N = int(input())


def check(k):
    r = N
    a = 0
    while 1:
        if r < k:
            a += r
            break
        r -= k
        a += k
        r -= r // 10
    return a * 2 >= N


left = 0
right = 10**18 + 1
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)
