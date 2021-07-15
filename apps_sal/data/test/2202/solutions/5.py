n, p = list(map(int, input().split()))
arr = list(map(int, input().split()))
sum_ = sum(arr)
res = 0
temp = 0
for i in arr:
    temp += i
    sum_ -= i
    res = max(res, temp % p + sum_ % p)

print(res)

