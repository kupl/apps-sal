def answer(a: str, b: str) -> str:
    if a == b:
        return 'EQUAL'

    if a < b or len(a) < len(b):
        return 'LESS'

    if a > b or len(a) > len(b):
        return 'GREATER'


def main():
    a = input()
    b = input()
    print(answer(a, b))


def __starting_point():
    main()
__starting_point()
