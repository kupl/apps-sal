read = lambda: list(map(int, input().split()))
n = int(input())
a = list(read())
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            print(j + 1, j + 2)
            a[j], a[j + 1] = a[j + 1], a[j]
