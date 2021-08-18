n = int(input())
x = list(map(int, input().split()))
for i in range(n - 1):
    a = sorted((x[i], x[i + 1]))
    for j in range(i):
        b = sorted((x[j], x[j + 1]))
        if b[0] < a[0] < b[1] < a[1] or a[0] < b[0] < a[1] < b[1]:
            print("yes")
            return
print("no")
