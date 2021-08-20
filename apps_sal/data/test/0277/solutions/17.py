(n, a, b) = [int(el) for el in input().split()]
for i in range(1, n + 1):
    if 2 ** i == n:
        n = i
        break
for i in range(1, n + 1):
    if (a - 1) // 2 ** i == (b - 1) // 2 ** i:
        if i == n:
            print('Final!')
        else:
            print(i)
        break
