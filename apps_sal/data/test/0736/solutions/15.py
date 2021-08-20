def main():
    nAndM = str(input()).split()
    (n, m) = (int(nAndM[0]), int(nAndM[1]))
    maxX = n // 2
    answers = []
    for x in range(maxX + 1):
        y = n - 2 * x
        if (x + y) % m == 0:
            answers.append(x + y)
        answers.sort()
    if answers:
        print(answers[0])
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
