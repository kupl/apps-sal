n = int(input())
res = 0
for i in range(n - 2):
    if int(n / (i + 2) - 1):
        res += 4 * (i + 2) * int(n / (i + 2) - 1)
print(res)
