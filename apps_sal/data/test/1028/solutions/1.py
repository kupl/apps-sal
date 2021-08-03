n, m = list(map(int, input().split()))

mod = n % m
min_size1 = (n // m)
min_size2 = min_size1 + 1
min_ans = min_size1 * (min_size1 - 1) // 2 * (m - mod) + min_size2 * (min_size2 - 1) // 2 * mod

max_ans = (n - m + 1) * (n - m) // 2

print(min_ans, max_ans)
