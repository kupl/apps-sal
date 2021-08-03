n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    z = [0] * n
    z[i] += 1
    j = i
    while z[j] != 2:
        j = a[j] - 1
        z[j] += 1
    print(j + 1, end=' ')
