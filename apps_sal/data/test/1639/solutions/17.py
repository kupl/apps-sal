n = int(input())
a = list(map(int, input().split()))
max_len = 0
cur_len = 0
cur = -1
for i in range(n):
    if a[i] >= cur:
        cur_len += 1
        cur = a[i]
        max_len = max(max_len, cur_len)
    else:
        cur = a[i]
        cur_len = 1
print(max_len)
