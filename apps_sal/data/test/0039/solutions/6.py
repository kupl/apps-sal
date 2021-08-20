from operator import eq


def is_palindrome(string):
    half = len(string) // 2 + 1
    return all(map(eq, string[:half], reversed(string)))


def main():
    string = input()
    first = string[0]
    if all((symbol == first for symbol in string)):
        print(0)
    else:
        print(len(string) - 1 if is_palindrome(string) else len(string))


main()
