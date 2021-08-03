n = int(input())
a = list(map(int, input().split()))
b = [0] * n
b[0] = a[0]
j = 1
for i in range(1, n):
    b[j] = a[i]
    while j > 0 and b[j] == b[j - 1]:
        j -= 1
        b[j] += 1
    j += 1
print(j)
for i in range(j):
    print(b[i], end=' ')
