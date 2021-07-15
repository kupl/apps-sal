n = int(input())
a = list(map(int, input().split()))

for i in reversed(list(range(len(a)))):
    for j in range(1, i + 1):
        if a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            print(j, j + 1)

