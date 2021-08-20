(n, m, k) = list(map(int, input().split()))
cnt = 0
count = 0
sum = 0
a = [int(s) for s in input().split()]
for i in range(n - 1, -1, -1):
    sum += a[i]
    if sum > k:
        sum = a[i]
        count += 1
        if count >= m:
            break
    cnt += 1
print(cnt)
