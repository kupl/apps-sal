def main():
    input()
    digits = list(map(int, input()))
    l = [digits]
    for a in range(1, 10):
        l.append([(a + b) % 10 for b in digits])
    for digits in l[:]:
        a = digits[-1]
        for (i, b) in enumerate(digits):
            if a and (not b):
                l.append(digits[i:] + digits[:i])
            a = b
    print(''.join(map(str, min(l))))


def __starting_point():
    main()


__starting_point()
