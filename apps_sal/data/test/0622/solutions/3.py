n, k = map(int, input().split())
i = 1
while (k % 2 == 0):
    k /= 2
    i += 1
print(i)
