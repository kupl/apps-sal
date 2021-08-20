def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main(n):
    m = 1
    while True:
        if not prime(m * n + 1):
            print(m)
            return
        m += 1


main(int(input()))
