n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

tot = 0
remain = 0
i = 0
while i < n:
    if a[i] + remain <= 8:
        tot += a[i] + remain
        remain = 0
    else:
        tot += 8
        remain += a[i] - 8
    if tot >= k:
        print(i + 1)
        break
    i += 1
if i == n:
    print(-1)
