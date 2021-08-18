
def main():
    N, K = list(map(int, input().split()))
    *A, = list(map(int, input().split()))

    def divisor_generator(n):
        div = 1

        stock = []
        while div * div <= n:
            if n % div == 0:
                yield n // div
                stock.append(div)
            div += 1

        for div in reversed(stock):
            yield div

    tot = sum(A)
    for div in divisor_generator(tot):
        k = tot // div - sum(a // div for a in A)
        R = sorted(a % div for a in A)
        Rc = [div - r for r in R]

        cond = (sr := sum(r for r in R[:N - k])) == sum(r for r in Rc[N - k:]) and sr <= K
        if cond:
            print(div)
            return


def __starting_point():
    main()


__starting_point()
