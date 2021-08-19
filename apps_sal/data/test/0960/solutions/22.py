(n, k) = map(int, input().split())


def nearest_div(n, k):
    for i in range(k - 1, -1, -1):
        if not n % i:
            return i


i = nearest_div(n, k)
print(k * (n // i) + i)
