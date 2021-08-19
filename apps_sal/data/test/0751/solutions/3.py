(n, m) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
i = 0
cnt = 0
while i < n:
    cur = m
    while i < n and a[i] <= cur:
        cur -= a[i]
        i += 1
    cnt += 1
print(cnt)
