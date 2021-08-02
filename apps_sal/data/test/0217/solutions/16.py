def main():
    A, B, F, K = list(map(int, input().split()))

    gas = B
    refuel = 0
    i = 1
    while i <= K:
        if i % 2:
            gas -= F
            if gas >= 0:
                if K - i > 0 and gas < (A - F) * 2 or \
                        K - i == 0 and gas < A - F:
                    gas = B
                    refuel += 1
                gas -= A - F
        else:
            gas -= A - F
            if gas >= 0:
                if K - i > 0 and gas < F * 2 or \
                        K - i == 0 and gas < F:
                    gas = B
                    refuel += 1
                gas -= F
        if gas < 0:
            print(-1)
            return
        i += 1

    print(refuel)


main()
