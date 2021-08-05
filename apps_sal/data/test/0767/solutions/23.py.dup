n, z = list(map(int, input().split()))
x = sorted(map(int, input().split()))

res, i, j = 0, 0, n // 2
while i < n // 2 and j < n:
    if x[i] + z <= x[j]:
        i += 1
        res += 1
    j += 1
print(res)
