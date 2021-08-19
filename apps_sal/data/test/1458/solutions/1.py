def main():
    n = int(input())
    s = list(input())
    for i in range(1, n):
        if ord(s[i]) < ord(s[i - 1]):
            print('YES')
            print(i, i + 1)
            return 0
    print('NO')
    return 0


main()
