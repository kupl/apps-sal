3


def main():
    data = input()
    n = int(input())

    if n > len(data):
        return "impossible"
    
    uniq = len(set(data))
    if n <= uniq:
        return "0"
    else:
        return n-uniq


def __starting_point(): print(main())

__starting_point()
