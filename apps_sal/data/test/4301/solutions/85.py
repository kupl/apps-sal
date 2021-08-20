def main():
    N = int(input())
    (fir, fir_i, sec, sec_i) = (0, 0, 0, 0)
    for i in range(N):
        tmp = int(input())
        if tmp > fir:
            sec = fir
            sec_i = fir_i
            fir = tmp
            fir_i = i
        elif tmp > sec:
            sec = tmp
            sec_i = i
    for i in range(N):
        if i != fir_i:
            print(fir)
        else:
            print(sec)


def __starting_point():
    main()


__starting_point()
