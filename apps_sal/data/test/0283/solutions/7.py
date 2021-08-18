
def main():
    import itertools

    def is_prime(x):
        if x == 2:
            return True
        if x & 0x1 == 0:
            return False
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

    try:
        while True:
            n = int(input())
            for m in itertools.count(1):
                if not is_prime(n * m + 1):
                    print(m)
                    break

    except EOFError:
        pass


main()
