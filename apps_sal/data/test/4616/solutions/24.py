def answer(s: str) -> str:
    return f'{s[0]}{len(s) - 2}{s[-1]}'

def main():
    s = input()
    print(answer(s))

def __starting_point():
    main()
__starting_point()
