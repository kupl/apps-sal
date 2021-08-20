def main():
    n = int(input())
    alphabets = 'zabcdefghijklmnopqrstuvwxy'
    answer_reversed = ''
    for i in range(100):
        idx = n % 26
        answer_reversed += alphabets[idx]
        if idx == 0:
            n -= 26
        else:
            n -= idx
        if n:
            n = n // 26
        else:
            break
    print(answer_reversed[::-1])


def __starting_point():
    main()


__starting_point()
