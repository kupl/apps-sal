A, B, X = list(map(int, input().split()))
# A, B, X = 10, 7, 100


def digit(x):
    strx = str(x)
    return len(strx)


def calc_value(x):
    return A * x + B * digit(x)


def binary_search(num_max):
    if num_max <= 0:
        return 0

    left = 0
    right = num_max
    while left <= right:
        mid = (left + right) // 2
        mid_value = calc_value(mid)
        if mid_value == X:
            return mid
        elif mid_value < X:
            left = mid + 1
        else:
            right = mid - 1

    return left-1


# data = list(range(0, X//A+1))
store = 10**9

if X >= calc_value(store):
    ans = store
else:
    ans = binary_search(X//A)
    ans = min(10**9, ans)

print(ans)

