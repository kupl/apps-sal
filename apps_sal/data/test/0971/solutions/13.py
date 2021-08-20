(n, b, d) = [int(i) for i in input().strip().split()]
a = [int(i) for i in input().strip().split()]
ans = 0
curr_size = 0
for i in range(n):
    if a[i] > b:
        continue
    curr_size += a[i]
    if curr_size > d:
        ans += 1
        curr_size = 0
print(ans)
