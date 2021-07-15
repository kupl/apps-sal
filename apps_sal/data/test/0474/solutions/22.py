
n = int(input())
arr = [int(x) for x in input().split()]
max_val = max(arr)

max_len = 0
cur_len = 0
for a in arr:
    if a == max_val:
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 0

print(max_len)

