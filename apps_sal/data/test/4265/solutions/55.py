def answer(s: str, t: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
            
    return count


def main():
    s = input()
    t = input()
    print((answer(s, t)))


def __starting_point():
    main()

__starting_point()
