(n, m) = list(map(int, input().split()))
max_dist = (n - 1) * n // 2
min_dist = max_dist
curr_value = max_dist
for i in range(n):
    curr_value = i * (i + 1) // 2 + (n - 1 - i) * (n - i) // 2
    min_dist = min(min_dist, curr_value)
answer = 0
add_value = 0
for i in range(m):
    (x, d) = list(map(int, input().split()))
    answer += x
    if d >= 0:
        add_value += d * max_dist
    else:
        add_value += d * min_dist
print(answer + add_value / n)
