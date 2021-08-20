(n, k) = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
med = n // 2


def key(m):
    s = 10 ** 10
    ind = None
    for i in range(n):
        if 0 <= m - array[i] <= s:
            s = m - array[i]
            ind = i
    if ind == None:
        return False
    if ind < med:
        return False
    else:
        for i in range(ind - 1, med - 1, -1):
            s += m - array[i]
        return s <= k


left = array[med]
right = 10 ** 10
while right - left != 1:
    mid = (right + left) // 2
    if key(mid):
        left = mid
    else:
        right = mid
print(left)
