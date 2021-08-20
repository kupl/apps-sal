(n, m) = [int(i) for i in input().split(' ')]
a = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]
x = int(input())
max_a = {}
for i in range(n):
    cur_sum = 0
    for j in range(i, n):
        cur_sum += a[j]
        if j - i + 1 not in max_a or cur_sum < max_a[j - i + 1]:
            max_a[j - i + 1] = cur_sum
max_b = {}
for i in range(m):
    cur_sum = 0
    for j in range(i, m):
        cur_sum += b[j]
        if j - i + 1 not in max_b or cur_sum < max_b[j - i + 1]:
            max_b[j - i + 1] = cur_sum
best_area = 0
for i in max_a:
    for j in max_b:
        cur_sum = max_a[i] * max_b[j]
        cur_area = i * j
        if cur_sum <= x:
            best_area = max(best_area, cur_area)
print(best_area)
