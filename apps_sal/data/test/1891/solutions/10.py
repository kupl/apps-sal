def ans(arr, l, r, a, b):
    if len(arr) == 0:
        return a
    if l == r:
        return len(arr) * b
    arr_left = []
    arr_right = []
    mid = (l + r) // 2
    for el in arr:
        if l <= el <= mid:
            arr_left += [el]
        if mid + 1 <= el <= r:
            arr_right += [el]
    return min(b * len(arr) * (r - l + 1), ans(arr_left, l, mid, a, b) + ans(arr_right, mid + 1, r, a, b))


n, k, a, b = list(map(int, input().split()))
arr = [int(i) - 1 for i in input().split()]

print(ans(arr, 0, (1 << n) - 1, a, b))
