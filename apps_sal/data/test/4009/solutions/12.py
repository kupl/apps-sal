n, x, y = [int(x) for x in input().split()]
a = [int(x) for x in list(input())]
counter = 0
for i in range(n - x, n):
    if i == n - y - 1:
        if a[i] == 0:
            counter += 1
    else:
        if a[i] == 1:
            counter += 1
print(counter)
