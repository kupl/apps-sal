n = int(input())
i = 1
j = 1
k = 0
while (i * j < n):
    if k % 2 == 0:
        i += 1
    else:
        j += 1
    k = 1 - k
print(i + j)
