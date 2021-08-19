n = int(input())
a = [0] + list(map(int, input().split())) + [1001]
res = 1
cur = 1
for i in range(n + 1):
    if a[i + 1] - a[i] == 1:
        cur += 1
    else:
        cur = 1
    res = max(res, cur)
print(max(0, res - 2))
