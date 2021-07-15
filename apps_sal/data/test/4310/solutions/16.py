a = sorted(list(map(int, input().split())), reverse=True)
res = 0
for i in range(3 - 1):
    res += a[i] - a[i + 1]
print(res)
