
T = int(input())


def spf(n):
    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            return i
    return n


for i in range(T):
    n = int(input())
    s = spf(n)
    print(n // s, (s - 1) * n // s)
