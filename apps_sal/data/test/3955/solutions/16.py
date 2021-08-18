
def __starting_point():
    n, k, p = map(int, input().split())
    numbers = list(map(int, input().split()))
    x = [0] * (n + 10)
    y = [0] * (n + 10)
    p = p ** k
    maxi = 0
    for i in range(n):
        x[i + 1] = numbers[i] | x[i]
    for j in range(n, -1, -1):
        y[j - 2] = numbers[j - 1] | y[j - 1]
    for i in range(n):
        if maxi < x[i] | numbers[i] * p | y[i]:
            maxi = x[i] | numbers[i] * p | y[i]
    print(maxi)


__starting_point()
