n = int(input())
res = 0
for i in range(1, n):
    res += (n - 1) // i
print(res)
