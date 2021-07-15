n = int(input())
a = 1
b = n * n
for i in range(n):
    for j in range(n // 2):
        print(a, b, end = ' ')
        a += 1
        b -= 1
    print()
