n, k = list(map(int, input().split()))

m = 2 * (n - 1) - k * (k - 1)

if m > 0:
    print(-1)

else:

    x = int((1 + (1 - 4 * m) ** 0.5) / 2)

    if x * (x - 1) + m > 0:
        x -= 1

    print(k - x)


# Made By Mostafa_Khaled
