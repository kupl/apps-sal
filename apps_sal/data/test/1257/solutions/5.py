3
(n, k) = [int(i) for i in input().split()]
total_sum = n * n - (n - k)
for row in range(1, n):
    row_right = n * n - row * (n - k + 1)
    val = row_right - (n - k)
    total_sum += val
print(total_sum)
next_l_num = 1
for row in range(1, n + 1):
    row_right = n * n - (row - 1) * (n - k + 1)
    next_r_num = row_right - (n - k)
    for col in range(1, n + 1):
        if col < k:
            print(next_l_num, end=' ')
            next_l_num += 1
        else:
            print(next_r_num, end=' ')
            next_r_num += 1
    print()
