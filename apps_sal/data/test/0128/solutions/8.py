#[int(i) for i in input().split()]
n, k = [int(i) for i in input().split()]
i = 0
res = 0
for j in range(min(n // 2, k)):
    res += n - j - 1 - j
    res += n - 2 - j - j
print(res)
