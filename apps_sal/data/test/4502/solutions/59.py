n = 4
a = [1, 2, 3, 4]

n = int(input())
a = input().split()


if n % 2 == 0:
    y = [a[j] for j in range(1, n, 2)][::-1]
    z = [a[j] for j in range(0, n, 2)]

else:
    y = [a[j] for j in range(0, n, 2)][::-1]
    z = [a[j] for j in range(1, n, 2)]

print((" ".join(map(str, y + z))))
