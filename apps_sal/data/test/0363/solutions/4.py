n = int(input())


def countd(n):
    d = 0
    while n >= 10**d:
        d += 1
    count = 0
    while d > 0:
        tens = 10 ** (d - 1)
        count += (n - tens + 1) * d
        n = tens - 1
        d -= 1
    return count


print(countd(n))
