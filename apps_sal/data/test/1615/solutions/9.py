n, k = list(map(int, input().split()))

sum = 0
for i in range(0, n):
    l, r = list(map(int, input().split()))
    sum += r - l + 1
if (sum % k == 0):
    res = sum
else:
    res = (sum // k + 1) * k
print(res - sum)
