n = int(input())
amount = 0
a = list(map(int, input().split()))
for i in range(n):
    for j in range(1, n):
        if a[j] < a[j - 1]:
            print(j, j + 1)
            amount += 1
            a[j], a[j - 1] = a[j - 1], a[j]
