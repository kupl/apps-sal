x, n = list(map(int, input().split()))
ways = 0


def permute(n, k):
    way = 1
    if n == k:
        return 1

    for i in range(n - k + 1, n + 1):
        way *= i

    return way


def combine(n, k):
    if n == k:
        return 1
    p = factorial(k)
    way = permute(n, k)
    return way / p


def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i

    return x


for _ in range(n):
    cart = input().strip()
    compartment = [6 for _ in range(9)]
    num = 0
    for i in range(36):
        if cart[i] == '1':
            compartment[num] -= 1

        if (i + 1) % 4 == 0:
            num += 1
    num -= 1
    for i in range(36, 54):
        if cart[i] == '1':
            compartment[num] -= 1

        if (i + 1) % 2 == 0:
            num -= 1

    for seat in compartment:
        if seat >= x:
            ways += combine(seat, x)

print(ways)
