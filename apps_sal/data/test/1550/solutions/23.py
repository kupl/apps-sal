def main():
    n = int(input())
    digits = list(map(int, input()))
    enum = [digits]
    for a in range(1, 10):
        enum.append([(a + b) % 10 for b in digits])
    for digits in enum[:10]:
        for j in range(n):
            if digits[j - 1] and not digits[j]:
                enum.append(digits[j:] + digits[:j])
    print(''.join(map(str, min(enum))))


def __starting_point():
    main()
__starting_point()
