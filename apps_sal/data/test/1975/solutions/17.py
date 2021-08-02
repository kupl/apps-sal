n, m = list(map(int, input().split()))

print(n + m - 1)
for i in range(m):
    print("1 " + str(i + 1))
for i in range(1, n):
    print(str(i + 1) + " 1")
