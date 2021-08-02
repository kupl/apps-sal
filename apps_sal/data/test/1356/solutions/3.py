def main():
    s = input()
    n = len(s)
    a = s.count('a')
    print(min(a + a - 1, n))
    return 0


main()
