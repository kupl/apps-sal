n = int(input())
m = n // 2 + 1
print(m)
(i, j) = (1, 1)
for _ in range(n):
    print(i, j)
    if i == j:
        j += 1
    else:
        i += 1
