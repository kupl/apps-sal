n = int(input())
k = 0
for i in range(1, n):
    k += (n - 1) // i
print(k)
