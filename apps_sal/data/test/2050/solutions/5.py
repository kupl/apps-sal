# input
n, k = map(int, input().split())

# variables

# main
print((6 * n - 1) * k)

for i in range(n):
    print(str((6 * i + 1) * k) + ' ' + str((6 * i + 2) * k) + ' ' + str((6 * i + 3) * k) + ' ' + str((6 * i + 5) * k))
