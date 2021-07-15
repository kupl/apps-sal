
def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        divisors.sort(reverse=True)
        return divisors

    N, M = list(map(int, input().split()))

    div = make_divisors(M)
    for d in div:
        if d <= M // N:
            print(d)
            break


def __starting_point():
    resolve()

__starting_point()
