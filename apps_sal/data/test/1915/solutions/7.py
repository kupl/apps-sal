n = int(input())

l = [1] * n

for i in range(1, n):
    for j in range(1, n):
        l[j] += l[j - 1]

print(l[n - 1])
