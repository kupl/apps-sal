input()
L = list(map(int, input().split()))
L.sort()
a = L[0]
k = 0
for i in L:
    for j in range(1, int(i ** 0.5 + 1)):
        if i % j == 0 and a + i - (i // j + a * j) > k:
            k = a + i - (i // j + a * j)
print(sum(L) - k)
