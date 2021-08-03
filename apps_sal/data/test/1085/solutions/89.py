def check(n, i):
    while n >= i and n % i == 0:
        n //= i
    return n % i == 1


def main():
    N = int(input())
    i = 2
    r = set()
    while i * i <= N:
        if N % i == 0:
            if check(N, i):
                r.add(i)
            if check(N, N // i):
                r.add(N // i)
        elif N % i == 1:
            r.add(i)
            if check(N, N // i):
                r.add(N // i)
        i += 1
    if N > 2:
        r.add(N - 1)
    r.add(N)
    return len(r)


print((main()))
