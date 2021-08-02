N = int(input())
l = 0
for i in range(3, N + 1, 2):
    j = 1
    k = 0
    while j * j < i:
        if i % j == 0:
            k += 2
        j += 2
    if j * j == i:
        k += 1
    if k == 8:
        l += 1
print(l)
