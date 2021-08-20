def main():
    s = input()
    score = 0
    diff = 0
    for i in range(len(s)):
        if s[i] == 'g':
            if diff == 0:
                diff += 1
            else:
                diff -= 1
                score += 1
        elif diff == 0:
            diff = 1
            score -= 1
        else:
            diff -= 1
    print(max(score, 0))


def __starting_point():
    main()


__starting_point()
