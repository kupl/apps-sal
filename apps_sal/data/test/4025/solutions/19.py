nums = [int(i) for i in input().split()]
(a, b, c) = (nums[0], nums[1], nums[2])
mode = 'abcacba'
min_weeks = 10 ** 9
min_weeks = min(min_weeks, a // 3)
min_weeks = min(min_weeks, b // 2)
min_weeks = min(min_weeks, c // 2)
(a, b, c) = (a - min_weeks * 3, b - min_weeks * 2, c - min_weeks * 2)
max_days = 0
for i in range(7):
    j = 0
    (left_a, left_b, left_c) = (a, b, c)
    while True:
        eat = mode[(i + j) % 7]
        if eat == 'a':
            if left_a == 0:
                break
            left_a -= 1
        elif eat == 'b':
            if left_b == 0:
                break
            left_b -= 1
        else:
            if left_c == 0:
                break
            left_c -= 1
        j += 1
    max_days = max(max_days, j)
print(min_weeks * 7 + max_days)
