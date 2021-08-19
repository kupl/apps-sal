(n, x, y) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(n):
    for j in range(max(i - x, 0), min(i + y + 1, n)):
        if a[j] <= a[i] and j != i:
            break
    else:
        print(i + 1)
        break
