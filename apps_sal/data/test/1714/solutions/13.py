a = input()
n, k = a.split(" ");
n = int(n)
k = int(k)
b = list()
b += [0]
for i in range(1, 2 * n + 1):
    b += [i]
for i in range(1, k + 1):
    b[2 * i], b[2 * i - 1] = b[2 * i - 1], b[2 * i]
for i in range(1, 2 * n + 1):
    print(b[i], end=" ")
