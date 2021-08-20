import bisect


def lower_bound(A, x):
    low = 0
    high = len(A)
    while low < high:
        mid = (low + high) // 2
        if int(A[mid]) < x:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(A, x):
    low = 0
    high = len(A)
    while low < high:
        mid = (low + high) // 2
        if int(A[mid]) <= x:
            low = mid + 1
        else:
            high = mid
    return low


line = input().split()
n = int(line[0])
x = int(line[1])
k = int(line[2])
a = [int(x) for x in input().split()]
a.sort()
ans = 0
for i in a:
    left = (i + x - 1) // x * x
    right = left + x * k - 1
    left = left + (k - 1) * x
    left = max(left, i)
    ans = ans + bisect.bisect_right(a, right) - bisect.bisect_left(a, left)
print(ans)
