n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(n - 1):
        if a[j + 1] < a[j]:
            (a[j], a[j + 1]) = (a[j + 1], a[j])
            print(j + 1, j + 2)
