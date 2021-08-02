n = int(input())
a = [0, -1, -1, -1, 1, -1, 1, -1, 2, 1, 2, -1, 3]
b = [3, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5, 4]
for i in range(n):
    x = int(input())
    if (x <= 12):
        print(a[x])
    else:
        print(((x - 12) // 12) * 3 + b[x % 12])
