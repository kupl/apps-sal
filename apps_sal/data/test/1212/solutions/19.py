(n, k) = input().split(' ')
a = input().split(' ')
sum = 0
for i in range(0, int(k)):
    sum += int(a[i])
res = sum
ans = 0
for i in range(int(k), int(n)):
    sum += int(a[i])
    sum -= int(a[i - int(k)])
    if sum < res:
        res = sum
        ans = i - int(k) + 1
print(ans + 1)
