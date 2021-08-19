n, m = map(int, input().split())
left = 0
right = 10000000
while right - left != 1:
    mid = (left + right) // 2
    # print(left, right)
    all_places = mid // 2 + mid // 3 - mid // 6
    if not(2 * n <= mid and 3 * m <= mid and n + m <= all_places):
        left = mid
    else:
        right = mid
print(right)
