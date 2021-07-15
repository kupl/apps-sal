n = int(input())
res = 0
for l in range(1, n):
    if (n - l) % l == 0:
        res += 1
print(res)
