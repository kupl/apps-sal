def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        if num == 0:
            print(1, 1)
        else:
            ok = False
            div = 1
            while div * div <= num:
                if num % div == 0:
                    add = max(num // div, div)
                    sub = min(num // div, div)
                    if (add + sub) % 2 == 0:
                        n = (add + sub) // 2
                        num_zeros = (add - sub) // 2
                        if num_zeros != 0:
                            k = n // num_zeros
                            if n ** 2 - (n // k) ** 2 == num:
                                ok = True
                                break
                div += 1
            if ok:
                print(n, k)
            else:
                print(-1)


def __starting_point():
    main()


__starting_point()
