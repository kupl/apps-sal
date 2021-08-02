n, d = list(map(int, input().split()))
a = sorted([list(map(int, input().split())) for i in range(n)])
left = 0
cur_sum = 0
max_sum = 0
for right in range(n):
    cur_sum += a[right][1]
    while a[right][0] - a[left][0] >= d:
        cur_sum -= a[left][1]
        left += 1
    if cur_sum > max_sum:
        max_sum = cur_sum
print(max_sum)
