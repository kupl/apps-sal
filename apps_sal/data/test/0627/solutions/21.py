def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        if ord(s[i - 1]) > ord(s[i]):
            return s[:(i - 1)] + s[i:]
    return s[:-1]


print(main())
